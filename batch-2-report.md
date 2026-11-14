# تقرير إنجاز الدفعة الثانية: معالجة الازدواجية والتشابه النصي (Batch 2 Deduplication Report)

- **الموقع:** شركة نجوم العرب لنقل الأثاث بجدة (`https://nojomalarab.com/`)
- **حالة الدفعة:** DONE بالكامل
- **طريقة التنفيذ:** تعديلات مباشرة وفورية داخل ملفات الصفحات الفعلية في الـ Working Tree (مكشوفة بالكامل في `git status` بدون أي commits وسيطة).

---

## 1. ملخص تنفيذ بنود الدفعة الثانية

| البند | الوصف | الحالة | الدليل / النتيجة |
|---|---|---|---|
| **B2-01** | حساب مصفوفة التشابه النصي قبل البدء | **DONE** | تم استخراج `similarity-before.csv` (أظهر تطابق الشقق والمكاتب بنسبة 99.97%). |
| **B2-02** | إعادة كتابة صفحات المكاتب والفلل من الصفر | **DONE** | إعادة كتابة `office-furniture-moving-jeddah` و `villa-moving-jeddah` بمحتوى متخصص وفريد بالكامل، فانخفض التشابه مع الشقق إلى **23.18% للمكاتب** و **29.75% للفلل**. |
| **B2-03** | صفحة الأسعار وتمايزها | **DONE** | تشابه صفحة الأسعار مع الشقق هو **32.05%** وجميعها < 40%، محتوية على الجداول والعوامل التسعة وحاسبة الأسعار بدون ادعاءات مضللة. |
| **B2-04** | دمج صفحة النجار وتوجيهها 301 | **DONE** | تطبيق الخيار A: إضافة 301 في `.htaccess`، تحديث كافة الروابط الداخلية (14 ملفاً)، وحذفها من `sitemap.xml`. |
| **B2-05** | إصلاح لغوي لصفحة "أفضل شركة" | **DONE** | تعديل كافة العناوين المكسورة لغوياً وحشو العبارات، وتأكيد دور الصفحة كدليل إرشادي محايد للاختيار. |
| **B2-06** | تدقيق نصوص الروابط الداخلية (Anchors) | **DONE** | توجيه العبارات الرئيسية العامة إلى الصفحة الرئيسية وتخصيص عبارات "أفضل شركة / دليل اختيار" واستخراج `anchors-report.csv` بـ 2710 روابط. |
| **B2-07** | دمج صفحة النقل بين المدن وتوجيهها 301 | **DONE** | تطبيق الخيار A: جعل `/intercity-moving/` هي الصفحة الحاضنة لجميع المسارات، إضافة 301 لـ `/intercity-furniture-moving-from-jeddah/`، وتحديث الروابط وخريطة الموقع. |
| **B2-08** | تمايز صفحات الخدمات التخصصية | **DONE** | تمايز نيات البحث في صفحات (الاقتصادي، التغليف، الشاحنات، الونش، التخزين) دون وعود "الأرخص". |
| **B2-09** | تدقيق وسوم Head و H1 | **DONE** | نتيجة فحص `scripts/check-head.py`: صفر أخطاء تكرار، ووسم H1 واحد فقط لكل صفحة. |
| **B2-10** | خريطة الكلمات المفتاحية والنيات | **DONE** | توليد ملف `keyword-map.csv` يوثق لكل صفحة الكلمة الأساسية والنية التسويقية مع صفر تنافس (No Cannibalization). |
| **B2-11** | توثيق التوجيهات 301 | **DONE** | إنشاء `redirects.md` وتضمين أوامر التحقق عبر `curl -I`. |

---

## 2. نتائج قياس التشابه النصي (Similarity Results)

### أعلى 10 أزواج تشابهاً بعد تنفيذ الدفعة (من واقع `similarity-after.csv`):
1. `areas/furniture-moving-hayu-alrawdah/` ↔ `areas/furniture-moving-hayu-alzahra/` (76.71%) - صفحات أحياء متجاورة
2. `areas/furniture-moving-in-hayu-alshati-jeddah/` ↔ `blogs/the-best-furniture-moving-company-in-jeddah/` (72.75%)
3. `areas/furniture-moving-hayu-al-safa/` ↔ `areas/furniture-moving-in-hayu-alshati-jeddah/` (72.64%)
4. `areas/furniture-moving-hayu-al-safa/` ↔ `blogs/the-best-furniture-moving-company-in-jeddah/` (70.91%)
5. `areas/furniture-moving-hayu-alnaeem/` ↔ `areas/hayu-almarwah/` (66.32%)
6. `areas/furniture-moving-hayu-alnaeem/` ↔ `areas/furniture-moving-hayu-alrawdah/` (64.26%)
7. `/` ↔ `/services/` (64.23%)
8. `areas/furniture-moving-hayu-alrawdah/` ↔ `areas/hayu-almarwah/` (63.38%)
9. `areas/furniture-moving-hayu-alsalama/` ↔ `areas/hayu-almarwah/` (63.23%)
10. `areas/furniture-moving-hayu-alzahra/` ↔ `areas/hayu-almarwah/` (63.09%)

> [!NOTE]
> **إنجاز فك الازدواجية لصفحات الخدمات:**
> - نقل الشقق ↔ نقل المكاتب: انخفض من **99.97%** إلى **23.18%**.
> - نقل الشقق ↔ نقل الفلل: انخفض إلى **29.75%**.
> - نقل المكاتب ↔ نقل الفلل: **20.60%**.
> لا يوجد أي زوج من صفحات الخدمات المستهدفة يتجاوز حاجز الـ 40%.

---

## 3. نتائج السكربتات الميدانية

1. **فحص الروابط والصور (`python scripts/check-links.py`):**
   - الروابط المفحوصة: **1441**
   - الروابط المكسورة أو المفقودة: **0** (ZERO MISSING).
2. **فحص الهيد والوسوم (`python scripts/check-head.py`):**
   - الصفحات المفحوصة: **51**
   - عناوين مكررة (Duplicate Titles): **0**
   - وصف مكرر (Duplicate Descriptions): **0**
   - عدم تطابق في Canonical: **0**
   - أخطاء H1 متعددة: **0**
3. **خريطة الموقع (`sitemap.xml`):**
   - تم تحديثها واستبعاد الصفحات التي تم دمجها وتحويلها (`/carpenter-furniture-disassembly-assembly-jeddah/` و `/intercity-furniture-moving-from-jeddah/`).

---

## 4. قائمة الملفات المسلمة ضمن الدفعة

- [batch-2-report.md](file:///c:/Users/HP/Desktop/my-work/day-1/nojomalarab/batch-2-report.md)
- [similarity-before.csv](file:///c:/Users/HP/Desktop/my-work/day-1/nojomalarab/similarity-before.csv)
- [similarity-after.csv](file:///c:/Users/HP/Desktop/my-work/day-1/nojomalarab/similarity-after.csv)
- [anchors-report.csv](file:///c:/Users/HP/Desktop/my-work/day-1/nojomalarab/anchors-report.csv)
- [keyword-map.csv](file:///c:/Users/HP/Desktop/my-work/day-1/nojomalarab/keyword-map.csv)
- [redirects.md](file:///c:/Users/HP/Desktop/my-work/day-1/nojomalarab/redirects.md)
- [facts-used.csv](file:///c:/Users/HP/Desktop/my-work/day-1/nojomalarab/facts-used.csv)
