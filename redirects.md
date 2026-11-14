# جدول عمليات إعادة التوجيه 301 - الدفعة الثانية (Batch 2 Deduplication)

يوثق هذا الملف قواعد إعادة التوجيه الدائمة 301 المنفذة في خادم الويب (Apache عبر `.htaccess`) لدمج الصفحات ذات المحتوى المتطابق أو المكرر وضمان توجيه محركات البحث والزوار للصفحات المعتمدة دون فقدان أرشفة أو روابط خارجية.

---

## 1. التوجيهات المنفذة في `.htaccess`

| الرابط القديم (المُعاد توجيهه) | الرابط الجديد المعتمد (الوجهة) | نوع التوجيه | السبب |
|---|---|---|---|
| `/carpenter-furniture-disassembly-assembly-jeddah/` | `https://nojomalarab.com/furniture-disassembly-and-reassembly-in-jeddah/` | 301 Permanent | دمج خدمة النجار ضمن صفحة الفك والتركيب الشاملة ومنع الافتراس |
| `/intercity-furniture-moving-from-jeddah/` | `https://nojomalarab.com/intercity-moving/` | 301 Permanent | دمج الدليل العام للنقل بين المدن مع الصفحة الرئيسية للمسارات |
| `/blogs/the-best-furniture-moving-company-in-jeddah/` | `https://nojomalarab.com/best-furniture-moving-company-jeddah/` | 301 Permanent | توجيه تدوينة أفضل شركة لصفحة الدليل الرئيسية |
| `/furniture-moving-across-jeddah's-neighborhoods-and-districts/` | `https://nojomalarab.com/furniture-moving-across-jeddahs-neighborhoods-and-districts/` | 301 Permanent | تصحيح مسار يحتوي على فاصلة عليا |

---

## 2. قواعد Apache .htaccess الفعلية

```apache
# عمليات إعادة توجيه الدفعة الثانية (دمج الصفحات المكررة)
Redirect 301 /carpenter-furniture-disassembly-assembly-jeddah/ https://nojomalarab.com/furniture-disassembly-and-reassembly-in-jeddah/
Redirect 301 /intercity-furniture-moving-from-jeddah/ https://nojomalarab.com/intercity-moving/
Redirect 301 /blogs/the-best-furniture-moving-company-in-jeddah/ https://nojomalarab.com/best-furniture-moving-company-jeddah/
Redirect 301 "/furniture-moving-across-jeddah's-neighborhoods-and-districts/" https://nojomalarab.com/furniture-moving-across-jeddahs-neighborhoods-and-districts/
```

---

## 3. أوامر التحقق والاختبار (cURL)

يمكن اختبار كل إعادة توجيه والتأكد من إرجاع كود الحالة `301 Moved Permanently` والرأس `Location` الصحيح عبر الأوامر التالية:

```bash
# اختبار توجيه صفحة النجار
curl -I https://nojomalarab.com/carpenter-furniture-disassembly-assembly-jeddah/

# اختبار توجيه صفحة النقل بين المدن
curl -I https://nojomalarab.com/intercity-furniture-moving-from-jeddah/

# اختبار تدوينة أفضل شركة
curl -I https://nojomalarab.com/blogs/the-best-furniture-moving-company-in-jeddah/
```
