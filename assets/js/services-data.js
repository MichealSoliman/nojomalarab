/**
 * نجوم العرب لنقل العفش بجدة - المصدر المركزي لخدمات الموقع والقائمة المنسدلة
 * 
 * لإضافة خدمة جديدة تظهر في القائمة المنسدلة بجميع الصفحات:
 * قم بإضافة عنصر جديد داخل مصفوفة SERVICES_DATA بالأسفل بنفس الهيكل:
 * {
 *     id: "معرف الخدمة",
 *     title: "عنوان الخدمة",
 *     url: "رابط الخدمة",
 *     icon: "أيقونة FontAwesome",
 *     desc: "وصف قصير للخدمة"
 * }
 */

window.SERVICES_DATA = [
    {
        id: "furniture-moving",
        title: "نقل عفش بجدة",
        url: "/best-furniture-moving-company-jeddah/",
        icon: "fa-solid fa-truck-moving",
        desc: "نقل الأثاث بأمان تام مع الفك والتركيب والتغليف باحترافية"
    },
    {
        id: "disassembly-reassembly",
        title: "فك وتركيب الأثاث بجدة",
        url: "/furniture-disassembly-and-reassembly-in-jeddah/",
        icon: "fa-solid fa-screwdriver-wrench",
        desc: "فك وتركيب جميع أنواع غرف النوم والأثاث والستائر والمطابخ"
    },
    {
        id: "packaging",
        title: "تغليف الأثاث بجدة",
        url: "/furniture-packaging-in-jeddah/",
        icon: "fa-solid fa-box-open",
        desc: "تغليف الأثاث والقطع الثمينة والزجاج بأفضل المواد لحمايتها"
    },
    {
        id: "storage",
        title: "تخزين الأثاث بجدة",
        url: "/furniture-storage-in-jeddah/",
        icon: "fa-solid fa-warehouse",
        desc: "مستودعات آمنة ومجهزة لتخزين الأثاث والعفش لفترات قصيرة وطويلة"
    },
    {
        id: "transport-trucks",
        title: "دينا نقل عفش بجدة",
        url: "/furniture-transport-trucks-in-jeddah/",
        icon: "fa-solid fa-truck-front",
        desc: "شاحنات ودينا نقل عفش مجهزة ومغلقة لمختلف أحجام المنقولات"
    },
    {
        id: "crane-moving",
        title: "ونش رفع عفش بجدة",
        url: "/furniture-lifting-crane-in-jeddah/",
        icon: "fa-solid fa-truck-monster",
        desc: "أوناش هيدروليكية لرفع وتنزيل الأثاث من وإلى الأدوار المرتفعة"
    },
    {
        id: "intercity-moving",
        title: "نقل عفش بين المدن من جدة",
        url: "/intercity-furniture-moving-from-jeddah/",
        icon: "fa-solid fa-route",
        desc: "شحن ونقل الأثاث لجميع مدن المملكة (الرياض، مكة، الشرقية، والجنوب)"
    },
    {
        id: "districts-moving",
        title: "نقل عفش بين أحياء جدة",
        url: "/areas/",
        icon: "fa-solid fa-map-location-dot",
        desc: "خدمات السريع والتغطية الشاملة لجميع أحياء ومناطق جدة"
    },
    {
        id: "villa-moving",
        title: "نقل فلل بجدة",
        url: "/villa-moving-jeddah/",
        icon: "fa-solid fa-house-chimney-window",
        desc: "خدمة متكاملة ونوعية لنقل وتجهيز الفلل والقصور بالكامل"
    },
    {
        id: "apartment-moving",
        title: "نقل شقق بجدة",
        url: "/apartment-furniture-moving-jeddah/",
        icon: "fa-solid fa-building",
        desc: "خدمة متكاملة ونوعية لنقل وتجهيز الشقق السكنية بالكامل"
    },
    {
        id: "carpenter-furniture-disassembly-assembly",
        title: " نجار فك وتركيب عفش بجدة",
        url: "/carpenter-furniture-disassembly-assembly-jeddah/",
        icon: "fa-solid fa-building",
        desc: "نجار مختص في فك وتركيب جميع أنواع الأثاث بجدة، عمالة ماهرة ومحترفة"
    },
   
    {
        id: "kitchen-moving-jeddah",
        title: " نقل مطابخ بجدة",
        url: "/kitchen-moving-jeddah/",
        icon: "fa-solid fa-utensils",
        desc: "خدمة نقل المطابخ بجدة تشمل فك وتركيب وتغليف ونقل المطابخ بأمان واحترافية."
    },
    {
        id: "affordable-furniture-moving-jeddah",
        title: "نقل عفش اقتصادي ",
        url: "/affordable-furniture-moving-jeddah/",
        icon: "fa-solid fa-utensils",
        desc: "نقل أثاث بأسعار مخفضة في جدة تشمل الفك والتركيب والتغليف والنقل بأمان واحترافية."
    },
];

(function () {
    // دالة لحساب الرابط المناسب سواء عبر السيرفر المحلي أو التصفح المباشر
    function getResolvedUrl(rawUrl) {
        if (!rawUrl) return '#';
        if (window.location.protocol === 'file:') {
            var pathname = window.location.pathname.replace(/\\/g, '/');
            var depth = 0;
            if (pathname.indexOf('/about/') !== -1) depth = 1;
            else if (pathname.indexOf('/services/') !== -1) depth = 1;
            else if (pathname.indexOf('/contact/') !== -1) depth = 1;
            else if (pathname.indexOf('/areas/') !== -1) {
                var parts = pathname.split('/areas/')[1].split('/').filter(Boolean);
                depth = (parts.length > 0 && parts[0].indexOf('.html') === -1) ? 2 : 1;
            }
            else if (pathname.indexOf('/furniture-') !== -1) depth = 1;
            else if (pathname.indexOf('/intercity-') !== -1) depth = 1;
            else if (pathname.indexOf('/villa-') !== -1) depth = 1;
            else if (pathname.indexOf('/apartment-') !== -1) depth = 1;
            else if (pathname.indexOf('/blogs/') !== -1) {
                var parts = pathname.split('/blogs/')[1].split('/').filter(Boolean);
                depth = (parts.length > 0 && parts[0].indexOf('.html') === -1) ? 2 : 1;
            }
            var prefix = depth === 2 ? '../../' : (depth === 1 ? '../' : './');
            return prefix + rawUrl.replace(/^\//, '');
        }
        return rawUrl;
    }

    // بناء القائمة المنسدلة للكمبيوتر والموبايل عند تجهيز الـ DOM
    function initServicesDropdown() {
        var services = window.SERVICES_DATA || [];
        var servicesMainUrl = getResolvedUrl('/services/');

        // --- 1. بناء القائمة المنسدلة للـ Desktop ---
        var navContainer = document.querySelector('nav#mainNav .hidden.lg\\:flex, nav .hidden.lg\\:flex');
        if (navContainer) {
            // البحث عن رابط "خدماتنا" السابق في القائمة
            var links = navContainer.querySelectorAll('a');
            var targetLink = null;
            links.forEach(function (link) {
                var text = link.textContent ? link.textContent.trim() : '';
                if (text.indexOf('خدماتنا') !== -1 || link.getAttribute('href') === './services/' || link.getAttribute('href') === '../services/' || link.getAttribute('href') === '/services/') {
                    targetLink = link;
                }
            });

            if (targetLink) {
                // إنشاء حاوية الدروب دون
                var dropdownWrapper = document.createElement('div');
                dropdownWrapper.className = 'relative group services-dropdown-wrapper py-2';

                // زر التفعيل الرئيسي
                var triggerLink = document.createElement('a');
                triggerLink.href = servicesMainUrl;
                triggerLink.className = 'relative px-4 py-2 text-gray-600 hover:text-secondary font-medium transition-all duration-300 flex items-center gap-1.5 cursor-pointer group-hover:text-secondary';
                triggerLink.setAttribute('aria-expanded', 'false');
                triggerLink.innerHTML = `
                    <span>خدماتنا</span>
                    <i class="fas fa-chevron-down text-[11px] transition-transform duration-300 services-arrow text-gray-400 group-hover:text-secondary"></i>
                    <span class="absolute bottom-0 right-1/2 transform translate-x-1/2 w-0 h-0.5 bg-secondary transition-all duration-300 group-hover:w-8"></span>
                `;

                // كارت القائمة المنسدلة مع جسر حماية لمنع الاختفاء عند التمرير
                var dropdownMenu = document.createElement('div');
                dropdownMenu.className = 'absolute right-0 top-full pt-2 w-[340px] sm:w-[380px] opacity-0 invisible transition-all duration-200 z-50 services-dropdown-menu';

                var innerCard = document.createElement('div');
                innerCard.className = 'bg-white rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.12),0_4px_12px_rgba(0,0,0,0.05)] border border-gray-100 p-2.5 ring-1 ring-black/5 overflow-hidden text-right';

                var headerHtml = `
                    <div class="px-3.5 py-2.5 mb-1.5 border-b border-gray-100 flex items-center justify-between bg-gradient-to-l from-amber-50/50 to-transparent rounded-xl">
                        <span class="flex items-center gap-2 text-primary font-bold text-xs">
                            <span class="w-6 h-6 rounded-md bg-amber-500/10 text-secondary flex items-center justify-center text-[11px]">
                                <i class="fas fa-layer-group"></i>
                            </span>
                            خدمات نجوم العرب
                        </span>
                        <span class="text-[10px] bg-amber-50 text-secondaryDark px-2.5 py-0.5 rounded-full font-bold border border-secondary/20">تغطية شاملة بجدة</span>
                    </div>
                `;

                var itemsHtml = '<div class="flex flex-col gap-1 services-dropdown-items p-1 text-right" style="max-height: 380px; overflow-y: auto; overscroll-behavior: contain; scroll-behavior: smooth; scrollbar-width: thin; scrollbar-color: #f59e0b #f8fafc;">';
                services.forEach(function (service) {
                    var itemUrl = getResolvedUrl(service.url);
                    itemsHtml += `
                        <a href="${itemUrl}" class="flex items-center justify-between gap-3 p-2.5 rounded-xl hover:bg-amber-50/70 border border-transparent hover:border-amber-100/80 transition-all duration-200 group/item text-right">
                            <div class="flex items-center gap-3 min-w-0">
                                <div class="w-9 h-9 rounded-xl bg-amber-50 text-secondary group-hover/item:bg-secondary group-hover/item:text-white flex items-center justify-center transition-all duration-200 shrink-0 shadow-xs">
                                    <i class="${service.icon} text-sm"></i>
                                </div>
                                <div class="flex flex-col text-right min-w-0">
                                    <span class="text-sm font-bold text-gray-800 group-hover/item:text-secondaryDark transition-colors leading-snug truncate">${service.title}</span>
                                    <span class="text-xs text-gray-500 line-clamp-1 mt-0.5">${service.desc}</span>
                                </div>
                            </div>
                            <i class="fas fa-chevron-left text-[10px] text-gray-300 opacity-0 -translate-x-1 group-hover/item:opacity-100 group-hover/item:translate-x-0 group-hover/item:text-secondary transition-all duration-200 shrink-0"></i>
                        </a>
                    `;
                });
                itemsHtml += '</div>';

                var footerHtml = `
                    <div class="mt-1.5 pt-2 border-t border-gray-100">
                        <a href="${servicesMainUrl}" class="flex items-center justify-between px-3.5 py-2.5 rounded-xl bg-gray-50 hover:bg-secondary/10 text-primary hover:text-secondaryDark font-bold text-xs transition-colors duration-200 group/footer">
                            <span class="flex items-center gap-2">
                                <i class="fas fa-arrow-left-long text-xs text-secondary group-hover/footer:-translate-x-1 transition-transform duration-200"></i>
                                <span>دليل كافة الخدمات والأسعار</span>
                            </span>
                            <span class="text-[10px] text-gray-400 group-hover/footer:text-secondary font-medium">عرض الكل</span>
                        </a>
                    </div>
                `;

                innerCard.innerHTML = headerHtml + itemsHtml + footerHtml;
                dropdownMenu.appendChild(innerCard);
                dropdownWrapper.appendChild(triggerLink);
                dropdownWrapper.appendChild(dropdownMenu);

                // أحداث الأمان والدعم للتمرير والضغط لمنع اختفاء القائمة
                var closeTimer = null;

                function openMenu() {
                    if (closeTimer) clearTimeout(closeTimer);
                    dropdownWrapper.classList.add('is-open');
                    triggerLink.setAttribute('aria-expanded', 'true');
                }

                function closeMenuWithDelay() {
                    if (closeTimer) clearTimeout(closeTimer);
                    closeTimer = setTimeout(function () {
                        dropdownWrapper.classList.remove('is-open');
                        triggerLink.setAttribute('aria-expanded', 'false');
                    }, 200);
                }

                // تفعيل الفتح فقط عند الوقوف على رابط خدماتنا في النافبار
                triggerLink.addEventListener('mouseenter', openMenu);
                triggerLink.addEventListener('mouseleave', closeMenuWithDelay);

                // الاستمرار في فتح القائمة طالما الماوس بداخلها
                dropdownMenu.addEventListener('mouseenter', openMenu);
                dropdownMenu.addEventListener('mouseleave', closeMenuWithDelay);

                triggerLink.addEventListener('click', function (e) {
                    if (window.innerWidth >= 1024) {
                        e.preventDefault();
                        if (dropdownWrapper.classList.contains('is-open')) {
                            dropdownWrapper.classList.remove('is-open');
                            triggerLink.setAttribute('aria-expanded', 'false');
                        } else {
                            openMenu();
                        }
                    }
                });

                document.addEventListener('click', function (e) {
                    if (!dropdownWrapper.contains(e.target)) {
                        dropdownWrapper.classList.remove('is-open');
                        triggerLink.setAttribute('aria-expanded', 'false');
                    }
                });

                // استبدال الرابط القديم بالدروب دون الجديد
                targetLink.parentNode.replaceChild(dropdownWrapper, targetLink);
            }
        }

        // --- 2. بناء القائمة المنسدلة للـ Mobile ---
        var mobileMenuContainer = document.querySelector('#mobileMenu .px-5.py-4, #mobileMenu .flex-col, #mobileMenu, #mobile-menu .flex-col, #mobile-menu, .mobile-menu');
        if (mobileMenuContainer) {
            var mobileLinks = mobileMenuContainer.querySelectorAll('a');
            var targetMobileLink = null;
            mobileLinks.forEach(function (link) {
                var text = link.textContent ? link.textContent.trim() : '';
                if (text.indexOf('خدماتنا') !== -1 || link.getAttribute('href') === './services/' || link.getAttribute('href') === '../services/' || link.getAttribute('href') === '/services/') {
                    targetMobileLink = link;
                }
            });

            if (targetMobileLink) {
                var mobileAccordion = document.createElement('div');
                mobileAccordion.className = 'w-full mobile-services-accordion';

                var mobileToggleBtn = document.createElement('button');
                mobileToggleBtn.type = 'button';
                mobileToggleBtn.className = 'w-full relative py-3 px-4 text-gray-700 hover:text-secondary font-medium transition-all duration-300 rounded-lg hover:bg-gray-50 flex items-center justify-between group';
                mobileToggleBtn.innerHTML = `
                    <div class="flex items-center gap-3">
                        <svg class="w-5 h-5 text-gray-400 group-hover:text-secondary transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
                        </svg>
                        <span>خدماتنا</span>
                    </div>
                    <i class="fas fa-chevron-down text-xs text-gray-400 transition-transform duration-300 mobile-services-arrow"></i>
                `;

                var mobileSubMenu = document.createElement('div');
                mobileSubMenu.className = 'mobile-services-sub hidden pr-3 pl-2 py-2 flex flex-col gap-1 border-r-2 border-secondary/30 mr-3 my-1 bg-gray-50/80 rounded-xl services-dropdown-items';
                mobileSubMenu.style.cssText = 'max-height: 320px; overflow-y: auto; overscroll-behavior: contain; scrollbar-width: thin; scrollbar-color: #f59e0b #f8fafc;';

                var subHtml = '';
                services.forEach(function (service) {
                    var itemUrl = getResolvedUrl(service.url);
                    subHtml += `
                        <a href="${itemUrl}" class="py-2 px-3 text-xs font-semibold text-gray-700 hover:text-secondaryDark hover:bg-white rounded-lg transition-all flex items-center justify-between group/mob">
                            <div class="flex items-center gap-2.5">
                                <i class="${service.icon} text-secondary text-xs w-4 text-center"></i>
                                <span>${service.title}</span>
                            </div>
                            <i class="fas fa-chevron-left text-[9px] text-gray-300 group-hover/mob:text-secondary transition-colors"></i>
                        </a>
                    `;
                });
                subHtml += `
                    <a href="${servicesMainUrl}" class="py-2 px-3 text-xs font-bold text-secondary bg-secondary/10 hover:bg-secondary hover:text-white rounded-lg transition-all flex items-center justify-between mt-1">
                        <span>عرض كافة الخدمات</span>
                        <i class="fas fa-arrow-left text-[10px]"></i>
                    </a>
                `;

                mobileSubMenu.innerHTML = subHtml;
                mobileAccordion.appendChild(mobileToggleBtn);
                mobileAccordion.appendChild(mobileSubMenu);

                // أحداث الفتح وإغلاق الأكورديون للموبايل
                mobileToggleBtn.addEventListener('click', function (e) {
                    e.preventDefault();
                    e.stopPropagation();
                    var isHidden = mobileSubMenu.classList.contains('hidden');
                    var arrow = mobileToggleBtn.querySelector('.mobile-services-arrow');

                    if (isHidden) {
                        mobileSubMenu.classList.remove('hidden');
                        if (arrow) arrow.style.transform = 'rotate(180deg)';
                    } else {
                        mobileSubMenu.classList.add('hidden');
                        if (arrow) arrow.style.transform = 'rotate(0deg)';
                    }

                    // تحديث ارتفاع الموبايل موني الحاوي إن وجد
                    var parentMobileMenu = document.getElementById('mobileMenu');
                    if (parentMobileMenu && parentMobileMenu.classList.contains('open')) {
                        parentMobileMenu.style.maxHeight = parentMobileMenu.scrollHeight + 'px';
                    }
                });

                targetMobileLink.parentNode.replaceChild(mobileAccordion, targetMobileLink);
            }
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initServicesDropdown);
    } else {
        initServicesDropdown();
    }
})();
