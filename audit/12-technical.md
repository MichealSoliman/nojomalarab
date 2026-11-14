# الفحص الفني الشامل للبنية التحتية وملفات التكوين (Technical SEO Analysis)
**الموقع:** https://nojomalarab.com/ (شركة نجوم العرب لنقل الأثاث بجدة)  
**تاريخ الفحص:** 2026-11-10  
**النطاق والأداة:** Antigravity Data & Technical Engine v2.0  

---

## 1. فحص ملف robots.txt
- **المسار المحلي:** `robots.txt`
- **الحالة الحالية:**
  ```txt
  User-agent: *
  Allow: /

  Sitemap: https://nojomalarab.com/sitemap.xml
  ```
- **التقييم التقني:**
  - سليم ومتوافق مع المعايير القياسية لمحركات البحث (RFC 9309).
  - يشير بشكل مباشر ودقيق إلى رابط خريطة الموقع `sitemap.xml`.
  - لا توجد قواعد حظر غير مقصودة لملفات الـ CSS أو JS أو الصور (`assets/`).
  - **التوصية:** الإبقاء عليه كما هو مع التأكد عند إضافة صفحات لوحة تحكم أو ملفات خاصة بالمستقبل بحجبها عبر `Disallow`.

---

## 2. فحص خريطة الموقع sitemap.xml
- **المسار المحلي:** `sitemap.xml`
- **عدد الروابط المدرجة:** 51 رابطاً.
- **عدد الصفحات الكلي في الموقع:** 54 صفحة (منها صفحة الخطأ 404.html ومكون الفوتر المستقل).
- **التقييم التقني:**
  - جميع الروابط تستخدم النطاق الموحد مع بروتوكول الأمان المشفر `https://nojomalarab.com/`.
  - جميع الروابط تنتهي بشرطة مائلة متوافقة مع الكانونيكال (Trailing Slash).
  - تم استبعاد صفحة الخطأ 404 بشكل صحيح لمنع إهدار ميزانية الزحف (Crawl Budget).
  - يتم تضمين علامات `lastmod` بصيغة ISO-8601 القياسية.

---

## 3. خادم الويب وملف التوجيه .htaccess
- **المسار المحلي:** `.htaccess`
- **القواعد المكتشفة:**
  1. إجبار بروتوكول الأمان HTTPS:
     ```apache
     RewriteCond %{HTTPS} off
     RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
     ```
  2. توحيد النطاق بدون www:
     ```apache
     RewriteCond %{HTTP_HOST} ^www\.nojomalarab\.com [NC]
     RewriteRule ^(.*)$ https://nojomalarab.com/$1 [L,R=301]
     ```
  3. التوجيه عند إزالة الامتداد `.html` وإضافة الـ Trailing Slash:
     - يضمن عدم وجود تكرار بين `example.com/page.html` و `example.com/page/`.
  4. ترويسات الأمان والحماية (Security Headers):
     - `X-Content-Type-Options: nosniff`
     - `X-Frame-Options: SAMEORIGIN`
     - `Referrer-Policy: strict-origin-when-cross-origin`
  5. التخزين المؤقت للمتصفح (Browser Caching / Mod_Expires):
     - تفعيل كاش طويل الأمد لملفات الصور والخطوط (1 سنة).
     - كاش لملفات CSS و JS (1 شهر).

---

## 4. أداء الموارد والوسائط والخطوط (Assets & Performance)
- **ملفات التنسيق (CSS):**
  - ملف وحيد مجمع ومنقى: `dist/output.css` (حجمه ~47KB)، مما يقلل طلبات HTTP ويحسن زمن FCP.
- **الخطوط (Typography):**
  - خط تجوال (Tajawal) يتم استدعاؤه مسبقاً عبر `preconnect` لـ `fonts.googleapis.com` و `fonts.gstatic.com` مع استخدام `display=swap`.
- **الصور (Images):**
  - جميع الصور الرئيسية بصيغة الحديثة `WebP`.
  - أبعاد محددة صراحة (`width` و `height`) على أكثر من 95% من الصور لمنع قفز التخطيط التراكمي (CLS = 0).
  - تفعيل `loading="lazy"` و `decoding="async"` على صور المحتوى غير الموجودة في الجزء المرئي الأول (Above the fold).

---

## 5. أكواد التتبع والتحليلات (Analytics & Tracking)
- **Google Tag (gtag.js):**
  - معرّف القياس الموحد: `G-60EE5N45S4`.
  - متواجد في الـ `<head>` عبر كامل صفحات الموقع.
- **ربط أزرار الاتصال والواتساب:**
  - يتم استخدام تتبع الأحداث (Event Tracking) عبر `onclick="gtag('event', 'click', ...)"` على أزرار الاتصال الهاتفي ونقرات الواتساب لضمان قياس التحويلات (Conversions) بدقة.

