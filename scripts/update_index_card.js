const fs = require('fs');
const path = require('path');

const indexPath = path.join(__dirname, '..', 'index.html');
let content = fs.readFileSync(indexPath, 'utf8');

const targetStr = `                                <h3
                                    class="text-2xl font-bold text-[#0a2540] mb-3 group-hover:text-orange-500 transition-colors duration-300">
                                    نقل العفش خارج جدة
                                </h3>

                                <p class="text-gray-600 leading-relaxed mb-4 text-sm">
                                    تغطية شاملة لجميع أحياء المدينة مع إمكانية النقل الآمن إلى المدن الأخرى بسهولة.
                                </p>

                                <div class="flex flex-wrap gap-2 mb-5">
                                    <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full">أحياء
                                        جدة</span>
                                    <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full">نقل بين
                                        المدن</span>
                                    <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full">تنظيم
                                        المواعيد</span>
                                </div>
                            </div>

                            <div class="mt-4">
                                <a href="./areas/"
                                    aria-label="تفاصيل خدمة النقل خارج جدة"
                                    class="w-full border-2 border-orange-500 text-orange-500 hover:bg-orange-500 hover:text-white px-4 py-2.5 rounded-xl text-xs font-semibold transition-all duration-300 text-center flex items-center justify-center gap-1.5">
                                    <span>تفاصيل النقل خارج جدة</span>`;

const replacementStr = `                                <h3
                                    class="text-2xl font-bold text-[#0a2540] mb-3 group-hover:text-orange-500 transition-colors duration-300">
                                    نقل العفش بين المدن
                                </h3>

                                <p class="text-gray-600 leading-relaxed mb-4 text-sm">
                                    رحلات شحن ونقل الأثاث من جدة إلى مختلف مدن المملكة كالعاصمة الرياض، مكة، المدينة، الطائف، والشرقية بشاحنات مجهزة.
                                </p>

                                <div class="flex flex-wrap gap-2 mb-5">
                                    <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full">نقل بين المدن</span>
                                    <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full">شاحنات مغلقة</span>
                                    <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full">تغطية شاملة</span>
                                </div>
                            </div>

                            <div class="mt-4">
                                <a href="./intercity-moving/"
                                    aria-label="دليل مسارات نقل العفش بين المدن من جدة"
                                    class="w-full border-2 border-orange-500 text-orange-500 hover:bg-orange-500 hover:text-white px-4 py-2.5 rounded-xl text-xs font-semibold transition-all duration-300 text-center flex items-center justify-center gap-1.5">
                                    <span>دليل مسارات النقل بين المدن</span>`;

// Normalize CRLF to LF for matching, then restore CRLF if needed
const isCRLF = content.includes('\r\n');
const normalizedContent = content.replace(/\r\n/g, '\n');
const normalizedTarget = targetStr.replace(/\r\n/g, '\n');
const normalizedReplacement = replacementStr.replace(/\r\n/g, '\n');

if (normalizedContent.includes(normalizedTarget)) {
    let updated = normalizedContent.replace(normalizedTarget, normalizedReplacement);
    if (isCRLF) {
        updated = updated.replace(/\n/g, '\r\n');
    }
    fs.writeFileSync(indexPath, updated, 'utf8');
    console.log('SUCCESS: Card 6 in index.html updated to Intercity Moving.');
} else {
    console.error('ERROR: Target string not found in index.html');
}
