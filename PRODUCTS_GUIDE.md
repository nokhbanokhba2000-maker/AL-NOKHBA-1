# 📦 دليل إضافة منتجات جديدة - موقع نخبة

## 🎯 طريقة إضافة منتج جديد

### 1️⃣ افتح ملف `single-page.html` وابحث عن:
```javascript
const allProducts = [
```
(يوجد في السطر رقم **504**)

---

### 2️⃣ أضف المنتج الجديد بهذا الشكل:

```javascript
{
    id: 17,                              // رقم تسلسلي فريد
    name: "اسم المنتج بالعربي",          // اسم المنتج
    category: "olive",                    // الفئة (انظر القائمة بالأسفل)
    price: 250,                           // السعر الحالي
    oldPrice: 300,                        // السعر قبل الخصم (احذفه لو مفيش خصم)
    discount: 17,                         // نسبة الخصم (احذفه لو مفيش خصم)
    weight: "١ كيلو",                    // الوزن/الحجم (اختياري)
    image: "رابط_صورة_المنتج.jpg",      // رابط الصورة من الموقع الأصلي أو رفعها
    available: true                       // true = متوفر، false = نفذت الكمية
},
```

---

### 3️⃣ أمثلة عملية:

#### مثال 1: منتج عادي بدون خصم
```javascript
{
    id: 20,
    name: "🫒 زيت زيتون بكر ممتاز ١ لتر",
    category: "olive",
    price: 450,
    weight: "١ لتر",
    image: "https://karimolive.shop/uploads/products/images/example.webp",
    available: true
},
```

#### مثال 2: منتج عليه خصم
```javascript
{
    id: 21,
    name: "صابون طبيعي بالزعتر",
    category: "soap",
    price: 45,
    oldPrice: 60,
    discount: 25,
    weight: "٢٥٠ جرام",
    image: "https://karimolive.shop/uploads/products/images/soap-example.webp",
    available: true
},
```

#### مثال 3: منتج غير متوفر
```javascript
{
    id: 22,
    name: "زيت الحبة السوداء",
    category: "natural-oils",
    price: 120,
    weight: "١٠٠ مل",
    image: "https://karimolive.shop/uploads/products/images/black-seed-oil.webp",
    available: false  // ← غير true لـ false لو نفذت الكمية
},
```

---

### 4️⃣ الفئات المتاحة (category):

| الفئة | الوصف |
|------|-------|
| `olive` | زيوت الزيتون |
| `hair` | زيوت الشعر |
| `soap` | الصابون الطبيعي |
| `offers` | العروض والخصومات |
| `spices` | التوابل والبهارات |
| `dates` | التمور |
| `nuts` | المكسرات واللب |
| `cosmetics` | مستحضرات التجميل |
| `honey` | العسل |
| `tea` | الشاي والبن |
| `herbs` | الأعشاب العلاجية |
| `zaytoun` | الزيتون المخلل |

---

### 5️⃣ بعد الإضافة:

1. احفظ الملف ✅
2. افتح المتصفح واضغط **Ctrl + F5** (Hard Refresh)
3. ابحث عن المنتج في خانة البحث للتأكد من ظهوره

---

## 💾 طريقة حفظ الصور

### الخيار 1: استخدام روابط مباشرة من الموقع الأصلي
```javascript
image: "https://karimolive.shop/uploads/products/images/your-image.webp"
```

### الخيار 2: رفع الصور محلياً
1. أنشئ مجلد `images` بجانب ملف HTML
2. ضع الصور فيه
3. استخدم الرابط المحلي:
```javascript
image: "./images/product-name.jpg"
```

---

## ⚠️ ملاحظات مهمة

- تأكد إن الـ `id` فريد وما يتكررش مع أي منتج تاني
- الأسعار تكون بالأرقام فقط (بدون ج.م أو فواصل)
- نسبة الخصم (`discount`) تكون رقم فقط
- `available: false` هيبطل يظهر زر "أضف للسلة" ويظهر "نفذت الكمية"

---

## 🔗 روابط مفيدة

- جميع صور المنتجات: https://karimolive.shop/uploads/products/images/
- صور الفئات: https://karimolive.shop/uploads/categories/
- آراء العملاء: https://karimolive.shop/uploads/reviews/images/
