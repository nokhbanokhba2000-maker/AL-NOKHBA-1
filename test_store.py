import http.server
import socketserver
import threading
import time
import urllib.request

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()

time.sleep(1)

try:
    response = urllib.request.urlopen(f"http://localhost:{PORT}/NOKHBA_Complete_Store.html")
    html = response.read().decode('utf-8')

    print("📡 اختبار السيرفر المحلي:")
    print(f"✅ حالة الاتصال: يعمل")
    print(f"📄 حجم الصفحة المستلمة: {len(html)} حرف")

    # Check key elements
    checks = [
        ("العنوان", "نخبة الشرق" in html),
        ("شريط الإعلانات", "التوصيل السريع" in html),
        ("منتج 1", "id: 1," in html),
        ("منتج 80", "id: 80," in html),
    ]

    print("\n🔍 عناصر التحقق:")
    for name, result in checks:
        status = "✅" if result else "❌"
        print(f"  {status} {name}")

except Exception as e:
    print(f"❌ خطأ في الاتصال: {e}")
finally:
    httpd.shutdown()
