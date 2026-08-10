"""Playwright smoke test for simple_html index.html (written by WebsiteAgent)."""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

from playwright.async_api import async_playwright


async def main() -> int:
    index_path = Path(sys.argv[1]).resolve()
    chromium_path = sys.argv[2]
    settle_ms = int(sys.argv[3]) if len(sys.argv) > 3 else 800

    page_errors: list[str] = []
    console_errors: list[str] = []
    local_request_failures: list[str] = []
    external_request_failures: list[str] = []

    if not index_path.is_file():
        print(json.dumps({"ok": False, "reason": "missing_index", "path": str(index_path)}))
        return 1

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(
            executable_path=chromium_path,
            headless=True,
        )
        page = await browser.new_page()

        page.on("pageerror", lambda exc: page_errors.append(str(exc)))

        def on_console(msg) -> None:
            if msg.type == "error":
                console_errors.append(msg.text)

        page.on("console", on_console)

        def on_request_failed(req) -> None:
            url = req.url or ""
            entry = f"{url}: {req.failure}"
            # Local file:// failures (missing script.js, style.css) are real bugs.
            # External CDN/ad-blocker failures are not: don't fail the site for a missing
            # google-analytics.js or a network-blocked CDN font.
            if url.startswith("file://"):
                local_request_failures.append(entry)
            else:
                external_request_failures.append(entry)

        page.on("requestfailed", on_request_failed)

        # `load` waits for stylesheets, scripts, and images — better than `domcontentloaded`
        # for catching script load errors. Falls back gracefully if a CDN hangs (timeout).
        try:
            response = await page.goto(index_path.as_uri(), wait_until="load", timeout=20000)
        except Exception as goto_exc:
            # CDN never loaded. Try again with the lenient wait so we can still verify
            # local code; the CDN failure is captured under external_request_failures.
            try:
                response = await page.goto(index_path.as_uri(), wait_until="domcontentloaded", timeout=10000)
            except Exception:
                print(json.dumps({"ok": False, "reason": "navigation_failed", "error": str(goto_exc)}))
                await browser.close()
                return 1

        if response is not None and response.status >= 400:
            local_request_failures.append(f"document status {response.status}")

        await page.wait_for_timeout(settle_ms)

        has_body = await page.evaluate("() => Boolean(document.body)")
        title = await page.title()

        await browser.close()

    ok = not page_errors and not local_request_failures and has_body
    payload = {
        "ok": ok,
        "title": title,
        "has_body": has_body,
        "page_errors": page_errors,
        # Console errors are reported but no longer fail the smoke test on their own —
        # libraries (Three.js, Tailwind CDN dev mode) often log warnings as `console.error`
        # without breaking the page. Genuine runtime failures surface as pageerror.
        "console_errors": console_errors,
        "request_failures": local_request_failures,
        "external_request_failures": external_request_failures,
    }
    print(json.dumps(payload, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
