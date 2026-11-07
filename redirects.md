# توثيق قواعد إعادة التوجيه 301 واختبارها (Redirects Audit)

تم إعداد قواعد التحويل وإعادة التوجيه الدائمة (HTTP 301 Permanent Redirect) في خادم Apache عبر ملف `.htaccess` لحماية سُلطة الموقع، وضمان مسار زحف موحد، ومنع تكرار المحتوى أو تشتت الـ Link Juice.

---

## 1. ملخص القواعد المُطبقة

| القاعدة | الرابط القديم / غير القياسي | الرابط المستهدف (301) | الغرض |
| :--- | :--- | :--- | :--- |
| **إجبار HTTPS** | `http://nojomalarab.com/services/` | `https://nojomalarab.com/services/` | أمان الاتصال وشهادة SSL |
| **منع www** | `https://www.nojomalarab.com/about/` | `https://nojomalarab.com/about/` | توحيد النطاق الرئيسي |
| **إزالة index.html** | `https://nojomalarab.com/contact/index.html` | `https://nojomalarab.com/contact/` | تجنب تكرار الصفحات والمظهر النظيف |
| **إضافة Trailing Slash** | `https://nojomalarab.com/services` | `https://nojomalarab.com/services/` | منع مشاكل الروابط النسبية وتوحيد الـ Canonical |
| **حل افتراس الكلمة** | `https://nojomalarab.com/blogs/the-best-furniture-moving-company-in-jeddah/` | `https://nojomalarab.com/best-furniture-moving-company-jeddah/` | توجيه إشارات البحث لصفحة الخدمة المستهدفة |
| **تصحيح الفاصلة العلوية** | `/furniture-moving-across-jeddah's-neighborhoods-and-districts/` | `/furniture-moving-across-jeddahs-neighborhoods-and-districts/` | تصحيح رابط غير قياسي به رمز اقتباس |

---

## 2. أوامر الفحص والتحقق بواسطة curl

يمكن تشغيل الأوامر التالية من سطر الأوامر (Terminal / Shell) للتحقق من كود الاستجابة `301 Moved Permanently` ووجهة التحويل `Location`:

### أ) فحص التحويل من HTTP إلى HTTPS:
```bash
curl -I http://nojomalarab.com/services/
```
**النتيجة المتوقعة:**
```http
HTTP/1.1 301 Moved Permanently
Location: https://nojomalarab.com/services/
```

### ب) فحص إزالة www:
```bash
curl -I https://www.nojomalarab.com/about/
```
**النتيجة المتوقعة:**
```http
HTTP/1.1 301 Moved Permanently
Location: https://nojomalarab.com/about/
```

### ج) فحص إزالة index.html:
```bash
curl -I https://nojomalarab.com/contact/index.html
```
**النتيجة المتوقعة:**
```http
HTTP/1.1 301 Moved Permanently
Location: https://nojomalarab.com/contact/
```

### د) فحص إضافة الشرطة المائلة (Trailing Slash):
```bash
curl -I https://nojomalarab.com/services
```
**النتيجة المتوقعة:**
```http
HTTP/1.1 301 Moved Permanently
Location: https://nojomalarab.com/services/
```

### هـ) فحص حل افتراس الكلمة المفتاحية:
```bash
curl -I https://nojomalarab.com/blogs/the-best-furniture-moving-company-in-jeddah/
```
**النتيجة المتوقعة:**
```http
HTTP/1.1 301 Moved Permanently
Location: https://nojomalarab.com/best-furniture-moving-company-jeddah/
```
