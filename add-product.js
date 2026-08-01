/**
 * 📦 دليل إضافة منتج جديد - موقع نخبة | NOKHBA
 * 
 * الموقع: /mnt/workspace/projects/nokhba/single-page.html
 * موقع بيانات المنتجات: السطر 504
 */

// ========================================
// طريقة الإضافة السريعة
// ========================================

// 1️⃣ افتح ملف single-page.html
// 2️⃣ ابحث عن: const allProducts = [
// 3️⃣ أضف المنتج الجديد قبل القوس }]

// ========================================
// هيكل المنتج (نموذج جاهز للنسخ)
// ========================================

const newProduct = {
    id: 17,                              // رقم تسلسلي (زياده على آخر رقم)
    name: "اسم المنتج بالعربي",         // اسم المنتج
    category: "olive",                   // الفئة (انظر القائمة بالأسفل)
    price: 250,                          // السعر الحالي
    oldPrice: null,                      // السعر القديم (اتركه null لو مفيش خصم)
    discount: null,                      // نسبة الخصم (اتركه null لو مفيش خصم)
    weight: "١ كيلو",                    // الوزن/الحجم (اختياري)
    image: "https://karimolive.shop/uploads/products/images/product-name.webp", // رابط الصورة
    available: true                      // true = متوفر، false = نفذت الكمية
};

// ========================================
// الفئات المتاحة
// ========================================
const categories = {
    olive: "🫒 زيوت الزيتون",
    hair: "💆‍♀️ زيوت الشعر",
    soap: "🧼 الصابون الطبيعي",
    offers: "🏷️ العروض والخصومات",
    spices: "🌶️ التوابل والبهارات",
    dates: "🌴 التمور",
    nuts: "🥜 المكسرات واللب",
    cosmetics: "💄 مستحضرات التجميل",
    honey: "🍯 العسل",
    tea: "🍵 الشاي والبن",
    herbs: "🌿 الأعشاب العلاجية",
    zaytoun: "🫒 الزيتون المخلل"
};

// ========================================
// أمثلة عملية جاهزة للنسخ
// ========================================

// مثال 1: زيت زيتون بدون خصم
/*
{
    id: 17,
    name: "🫒 زيت زيتون بكر ممتاز ١ لتر",
    category: "olive",
    price: 450,
    weight: "١ لتر",
    image: "https://karimolive.shop/uploads/products/images/example.webp",
    available: true
},
*/

// مثال 2: منتج عليه خصم
/*
{
    id: 18,
    name: "صابون طبيعي بالزعتر",
    category: "soap",
    price: 45,
    oldPrice: 60,
    discount: 25,
    weight: "٢٥٠ جرام",
    image: "https://karimolive.shop/uploads/products/images/soap-example.webp",
    available: true
},
*/

// مثال 3: منتج غير متوفر
/*
{
    id: 19,
    name: "زيت الحبة السوداء",
    category: "natural-oils",
    price: 120,
    weight: "١٠٠ مل",
    image: "https://karimolive.shop/uploads/products/images/black-seed-oil.webp",
    available: false
},
*/

// ========================================
// خطوات الإضافة
// ========================================
/*
1. افتح الملف: /mnt/workspace/projects/nokhba/single-page.html
2. ابحث عن السطر 520 (بعد آخر منتج)
3. أضف فاصلة بعد آخر منتج: },
4. ألصق كود المنتج الجديد
5. احفظ الملف (Ctrl+S)
6. افتح المتصفح واضغط Ctrl+F5 للتحديث
*/

// ========================================
// روابط الصور المفيدة
// ========================================
const imageSources = {
    products: "https://karimolive.shop/uploads/products/images/",
    categories: "https://karimolive.shop/uploads/categories/",
    reviews: "https://karimolive.shop/uploads/reviews/images/"
};

console.log("✅ تم تحميل دليل إضافة المنتجات");
console.log("📍 موقع البيانات: السطر 504 في single-page.html");
console.log("📚 اقرأ الدليل الكامل: PRODUCTS_GUIDE.md");
