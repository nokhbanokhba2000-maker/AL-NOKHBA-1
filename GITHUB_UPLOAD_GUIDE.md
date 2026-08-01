# 🚀 دليل رفع المشروع على GitHub

## الخطوة 1: إعداد Git (تم بالفعل)
```bash
cd /mnt/workspace/projects/nokhba
git status
```

## الخطوة 2: ربط المستودع البعيد
```bash
git remote add origin https://github.com/nokhbanokhba2000-maker/-nokhba_2.git
git branch -M main
```

## الخطوة 3: رفع المشاريع
### الطريقة الأولى: باستخدام Personal Access Token (موصى به)
```bash
git push https://<YOUR_GITHUB_TOKEN>@github.com/nokhbanokhba2000-maker/-nokhba_2.git main
```

### الطريقة الثانية: باستخدام SSH
```bash
# أضف مفتاح SSH到你的GitHub账户
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub  # انسخ المفتاح

# ثم اربط بالمستودع
git remote set-url origin git@github.com:nokhbanokhba2000-maker/-nokhba_2.git
git push -u origin main
```

## الخطوة 4: التحقق من الرفع
افتح المتصفح واذهب إلى:
https://github.com/nokhbanokhba2000-maker/-nokhba_2

---

## 📁 محتويات المستودع

```
-nokhba_2/
├── single-page.html      (الصفحة الرئيسية - 50KB)
├── admin.html            (لوحة تحكم المنتجات - 31KB) ⭐ جديد
├── index.html            (الصفحة الرئيسية المنفصلة - 62KB)
├── products.html         (صفحة المنتجات - 56KB)
├── PAYMENT_INFO.md       (معلومات الدفع - 3KB) ⭐ جديد
├── PRODUCTS_GUIDE.md     (دليل إضافة المنتجات)
├── WEBSITE_AGENT_GUIDE.md (دليل Website Agent)
└── README.md             (تعليمات عامة)
```

---

## 🔗 الروابط المفيدة

| الخدمة | الرابط |
|--------|--------|
| GitHub Repository | https://github.com/nokhbanokhba2000-maker/-nokhba_2 |
| لوحة التحكم | `/admin.html` |
| الموقع الرئيسي | `/single-page.html` |
| WhatsApp | https://wa.me/201023696962 |

---

## 💡 نصائح للـ Website Agent

عند استخدام Website Agent لبناء الموقع نهائياً:
1. اعطه ملف `WEBSITE_AGENT_GUIDE.md` للتفاصيل الكاملة
2. استخدم `admin.html` لإدارة المنتجات
3. الرقم الجديد: **01023696962**
4. طرق الدفع: واتساب + إنستا باي