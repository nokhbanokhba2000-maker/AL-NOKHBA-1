# 🚀 خطوات رفع المشروع على GitHub - دليل مصور

## المستودع المستهدف:
**https://github.com/nokhbanokhba2000-maker/-nokhba_2.git**

---

## الطريقة الأسهل: استخدام GitHub Desktop

### الخطوة 1: تحميل GitHub Desktop
1. اذهب إلى: https://desktop.github.com/
2. حمل الملف وثبته
3. افتح البرنامج وسجل الدخول بحساب GitHub الخاص بك

### الخطوة 2: إضافة المستودع المحلي
1. في GitHub Desktop، اضغط على **File > Add Local Repository**
2. اختر المجلد: `/mnt/workspace/projects/nokhba`
3. اضغط **Add Repository**

### الخطوة 3: ربط بالمستودع البعيد
1. اضغط على **Repository > Repository Settings**
2. في قسم **Remote**، اضغط على **Add remote**
3. الاسم: `origin`
4. URL: `https://github.com/nokhbanokhba2000-maker/-nokhba_2.git`
5. اضغط **Add remote**

### الخطوة 4: رفع المشروع
1. اكتب وصف للcommitted (مثال: "Initial commit: NOKHBA store")
2. اضغط **Commit to main**
3. اضغط على **Push origin** في الأعلى
4. انتظر حتى ينتهي الرفع

### الخطوة 5: التحقق
افتح المتصفح واذهب إلى:
**https://github.com/nokhbanokhba2000-maker/-nokhba_2**

---

## الطريقة الثانية: عبر Terminal (للمتقدمين)

```bash
# 1. اذهب لمجلد المشروع
cd /mnt/workspace/projects/nokhba

# 2. تحقق من حالة Git
git status

# 3. أضف جميع الملفات
git add .

# 4. قم بعمل commit
git commit -m "Initial commit: NOKHBA e-commerce store with admin panel"

# 5. اربط بالمستودع البعيد
git remote add origin https://github.com/nokhbanokhba2000-maker/-nokhba_2.git

# 6. ارفع المشروع
git push -u origin main
```

**ملاحظة:** سيطلب منك username و password/token من GitHub.

---

## طريقة الحصول على GitHub Token (إذا لزم الأمر)

1. اذهب إلى: https://github.com/settings/tokens
2. اضغط على **Generate new token (classic)**
3. اختر expiration: No expiration
4. ضع علامة على: `repo` (Full control of private repositories)
5. اضغط **Generate token**
6. انسخ الـ token واستخدمه مكان كلمة المرور عند الرفع

---

## بعد الرفع بنجاح

✅ ستجد جميع الملفات على GitHub:
- single-page.html (الموقع الرئيسي)
- admin.html (لوحة تحكم المنتجات)
- جميع ملفات التوثيق

🎉 يمكنك بعد ذلك:
- استخدام GitHub Pages لاستضافة مجانية
- مشاركة الرابط مع فريقك
- العمل عليه معاً بشكل متزامن