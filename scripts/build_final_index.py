import json

with open('scripts/schema.json', 'r', encoding='utf-8') as f:
    schema_str = f.read()

# Build the complete final index.html
html_content = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="theme-color" content="#0a2540">

    <!-- 1. Title (64 حرفاً - الكلمة الرئيسية في المقدمة مع الحفاظ على الهوية) -->
    <title>شركة نقل عفش جدة | نقل أثاث بجدة فك وتغليف وتركيب - نجوم العرب</title>

    <!-- 2. Meta Description (148 حرفاً) -->
    <meta name="description"
        content="شركة نقل عفش جدة – نجوم العرب: نقل أثاث مع فك وتركيب وتغليف للشقق والفلل والمكاتب بسيارات مجهزة في كل أحياء جدة. معاينة مجانية: 0500504024">

    <!-- 3. Robots -->
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="googlebot" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">

    <!-- 4. Canonical -->
    <link rel="canonical" href="https://nojomalarab.com/">

    <!-- 5. Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:locale" content="ar_SA">
    <meta property="og:site_name" content="شركة نجوم العرب لنقل الأثاث بجدة">
    <meta property="og:title" content="شركة نقل عفش جدة | نقل أثاث بجدة فك وتغليف وتركيب - نجوم العرب">
    <meta property="og:description"
        content="شركة نقل عفش جدة – نجوم العرب: نقل أثاث مع فك وتركيب وتغليف للشقق والفلل والمكاتب بسيارات مجهزة في كل أحياء جدة. معاينة مجانية: 0500504024">
    <meta property="og:url" content="https://nojomalarab.com/">
    <meta property="og:image" content="https://nojomalarab.com/assets/img/og-image.webp">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/webp">
    <meta property="og:image:alt" content="أسطول سيارات وفريق شركة نجوم العرب لنقل العفش والأثاث بجدة">

    <!-- 6. Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="شركة نقل عفش جدة | نقل أثاث بجدة فك وتغليف وتركيب - نجوم العرب">
    <meta name="twitter:description"
        content="شركة نقل عفش جدة – نجوم العرب: نقل أثاث مع فك وتركيب وتغليف للشقق والفلل والمكاتب بسيارات مجهزة في كل أحياء جدة. معاينة مجانية: 0500504024">
    <meta name="twitter:image" content="https://nojomalarab.com/assets/img/og-image.webp">
    <meta name="twitter:image:alt" content="أسطول سيارات وفريق شركة نجوم العرب لنقل العفش والأثاث بجدة">

    <!-- 7. Favicon -->
    <link rel="icon" type="image/webp" href="/assets/img/logo-128.webp">
    <link rel="apple-touch-icon" href="/assets/img/logo-512.webp">

    <!-- 8. Resource Preloads -->
    <link rel="preload" href="/assets/fonts/Tajawal-Bold.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/assets/fonts/Tajawal-Regular.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/assets/fonts/Tajawal-Medium.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" as="image" href="/assets/img/hero-1200.webp"
        imagesrcset="/assets/img/hero-480.webp 480w, /assets/img/hero-768.webp 768w, /assets/img/hero-1200.webp 1200w"
        imagesizes="(max-width: 768px) 100vw, 50vw" fetchpriority="high">

    <!-- 9. Stylesheet (output.css only, Font Awesome removed) -->
    <link rel="stylesheet" href="/dist/output.css">

    <!-- 10. Analytics Script -->
    <script src="/assets/js/analytics.js" defer></script>

    <!-- 11. Schema Markup (JSON-LD) -->
    <script type="application/ld+json">
{schema_str}
    </script>
</head>

<body class="bg-white text-gray-800 font-sans antialiased overflow-x-hidden">

    <!-- Skip Link for Accessibility -->
    <a href="#main-content"
        class="sr-only focus:not-sr-only focus:fixed focus:top-4 focus:right-4 focus:z-50 focus:bg-orange-500 focus:text-white focus:px-4 focus:py-2 focus:rounded-lg focus:shadow-xl focus:outline-none focus:ring-2 focus:ring-white">
        تخطي إلى المحتوى الرئيسي
    </a>

    <!-- Header Navigation -->
    <header class="sticky top-0 z-40 bg-[#0a2540] border-b border-gray-800 shadow-lg">
        <div class="container mx-auto px-4 md:px-8 lg:px-16">
            <div class="flex items-center justify-between h-20">

                <!-- Logo & Brand Identity -->
                <a href="https://nojomalarab.com/" class="flex items-center gap-3.5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400 rounded-xl p-1"
                    aria-label="الرئيسية - شركة نجوم العرب لنقل الأثاث بجدة" aria-current="page">
                    <img src="/assets/img/logo-128.webp" alt="شعار شركة نجوم العرب لنقل الأثاث بجدة" width="56" height="56"
                        class="w-12 h-12 sm:w-14 sm:h-14 rounded-full object-contain bg-white/5 border border-white/10 p-1">
                    <div class="flex flex-col">
                        <span class="text-lg sm:text-xl font-extrabold text-white tracking-wide">نجوم العرب</span>
                        <span class="text-xs text-orange-400 font-medium">نقل أثاث بجدة</span>
                    </div>
                </a>

                <!-- Desktop Navigation Menu -->
                <nav class="hidden xl:flex items-center gap-6 text-sm font-semibold text-gray-200"
                    aria-label="التنقل الرئيسي">
                    <a href="https://nojomalarab.com/" aria-current="page"
                        class="text-orange-400 hover:text-white transition-colors">الرئيسية</a>
                    <a href="#about" class="hover:text-orange-400 transition-colors">من نحن</a>
                    <a href="./services/" class="hover:text-orange-400 transition-colors">خدماتنا</a>
                    <a href="./office-furniture-moving-jeddah/" class="hover:text-orange-400 transition-colors">مكاتب وشركات</a>
                    <a href="./furniture-moving-prices-jeddah/" class="hover:text-orange-400 transition-colors">أسعار نقل العفش</a>
                    <a href="./areas/" class="hover:text-orange-400 transition-colors">أحياء جدة</a>
                    <a href="./blogs/" class="hover:text-orange-400 transition-colors">المدونة</a>
                    <a href="#whyus" class="hover:text-orange-400 transition-colors">لماذا نحن</a>
                    <a href="#faq" class="hover:text-orange-400 transition-colors">الأسئلة</a>
                    <a href="./contact/" class="hover:text-orange-400 transition-colors">تواصل معنا</a>
                </nav>

                <!-- Desktop CTA & Mobile Toggle -->
                <div class="flex items-center gap-3">
                    <a href="tel:+966500504024" aria-label="اتصل بنا الآن على رقم 0500504024"
                        class="hidden sm:inline-flex items-center gap-2 bg-orange-500 hover:bg-orange-600 text-white text-sm font-bold px-5 py-2.5 rounded-full transition-colors shadow-md">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24" aria-hidden="true">
                            <path
                                d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1.003 1.003 0 011.02-.24c1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z" />
                        </svg>
                        <span>0500504024</span>
                    </a>

                    <!-- Mobile Menu Button -->
                    <button id="mobileMenuBtn" type="button" aria-expanded="false" aria-controls="mobileMenu"
                        aria-label="فتح القائمة الرئيسية"
                        class="xl:hidden p-2 text-gray-300 hover:text-white rounded-lg hover:bg-white/5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Navigation Menu -->
        <div id="mobileMenu"
            class="hidden xl:hidden bg-[#0a2540] border-t border-gray-800 px-4 py-6 transition-all duration-300 shadow-2xl overflow-y-auto"
            style="max-height: calc(100dvh - 80px);" aria-label="قائمة الهاتف">
            <nav class="flex flex-col gap-4 text-base font-semibold text-gray-200">
                <a href="https://nojomalarab.com/" aria-current="page"
                    class="text-orange-400 hover:text-white py-2 border-b border-gray-800">الرئيسية</a>
                <a href="#about" class="hover:text-orange-400 py-2 border-b border-gray-800">من نحن</a>
                <a href="./services/" class="hover:text-orange-400 py-2 border-b border-gray-800">خدماتنا</a>
                <a href="./office-furniture-moving-jeddah/" class="hover:text-orange-400 py-2 border-b border-gray-800">نقل مكاتب وشركات</a>
                <a href="./furniture-moving-prices-jeddah/" class="hover:text-orange-400 py-2 border-b border-gray-800">أسعار نقل العفش</a>
                <a href="./areas/" class="hover:text-orange-400 py-2 border-b border-gray-800">أحياء جدة</a>
                <a href="./blogs/" class="hover:text-orange-400 py-2 border-b border-gray-800">المدونة</a>
                <a href="#whyus" class="hover:text-orange-400 py-2 border-b border-gray-800">لماذا نحن</a>
                <a href="#faq" class="hover:text-orange-400 py-2 border-b border-gray-800">الأسئلة الشائعة</a>
                <a href="./contact/" class="hover:text-orange-400 py-2 border-b border-gray-800">تواصل معنا</a>

                <div class="pt-4 flex flex-col gap-3">
                    <a href="tel:+966500504024"
                        class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 rounded-xl text-center flex items-center justify-center gap-2">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1.003 1.003 0 011.02-.24c1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                        <span>اتصل بنا: 0500504024</span>
                    </a>
                    <a href="https://wa.me/966500504024" target="_blank" rel="noopener noreferrer"
                        class="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-3 rounded-xl text-center flex items-center justify-center gap-2">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.205 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                        <span>تواصل عبر واتساب</span>
                    </a>
                </div>
            </nav>
        </div>
    </header>

    <main id="main-content">
        <!-- B. Hero Section -->
        <section id="home" class="relative bg-[#0a2540] py-16 sm:py-24 lg:py-28 flex items-center"
            aria-label="الرئيسية - خدمات نقل العفش بجدة">
            <div class="container mx-auto px-4 md:px-8 lg:px-16 relative z-10">
                <div class="flex flex-col lg:flex-row items-center justify-between gap-12 lg:gap-16">

                    <!-- Content Column -->
                    <div class="flex-1 text-center lg:text-right">
                        <!-- Badge -->
                        <div
                            class="inline-flex items-center gap-2.5 bg-white/10 text-orange-400 text-sm sm:text-base font-semibold px-6 py-2.5 rounded-full mb-6 backdrop-blur-sm border border-white/10">
                            <span class="w-2.5 h-2.5 rounded-full bg-orange-400" aria-hidden="true"></span>
                            <span>خدمات نقل الأثاث والعفش داخل جدة وضواحيها</span>
                        </div>

                        <!-- Single H1 Heading (Exact Match) -->
                        <h1
                            class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-4 tracking-tight">
                            شركة نقل عفش جدة
                        </h1>

                        <!-- Subheading / Company Title (Diversified Synonym) -->
                        <p class="text-xl sm:text-2xl lg:text-3xl text-orange-400 font-bold mb-6">
                            نقل أثاث بجدة بخبرة وسيارات مجهزة — نجوم العرب
                        </p>

                        <!-- Concise Description (48 words natural on-page SEO text with single strong) -->
                        <p
                            class="text-base sm:text-lg lg:text-xl text-gray-200 leading-relaxed max-w-2xl mx-auto lg:mx-0 mb-8">
                            تقدم نجوم العرب، بصفتها <strong>شركة نقل عفش جدة</strong> موثوقة، حلولاً متكاملة في نقل أثاث المنازل مع خدمات فك وتركيب وتغليف مخصصة لتلبية احتياجات الشقق والفلل والمكاتب. نعتمد على سيارات دينا مجهزة وأطقم فنية خبيرة مع توفير معاينة مجانية لضمان انتقال آمن ومنظم لجميع مقتنياتك.
                        </p>

                        <!-- Quick Features List (Inline SVGs) -->
                        <div
                            class="flex flex-wrap items-center justify-center lg:justify-start gap-3 mb-10 text-xs sm:text-sm text-gray-200 font-medium">
                            <div class="flex items-center gap-2 bg-white/10 px-4 py-2.5 rounded-xl border border-white/10">
                                <svg class="w-4 h-4 text-orange-400" fill="currentColor" viewBox="0 0 24 24"><path d="M20 8h-3V4H1v13h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zm-5-2v2h-4V6h4zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm13.5-9l1.96 2.5H17V9.5h2.5zm-1.5 9c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>
                                <span>دينا نقل عفش مجهزة</span>
                            </div>
                            <div class="flex items-center gap-2 bg-white/10 px-4 py-2.5 rounded-xl border border-white/10">
                                <svg class="w-4 h-4 text-orange-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M11 4a2 2 0 114 0v1a2 2 0 01-2 2 2 2 0 01-2-2V4zm2 6a2 2 0 012 2v7a2 2 0 01-2 2 2 2 0 01-2-2v-7a2 2 0 012-2z"/></svg>
                                <span>فك وتركيب الأثاث</span>
                            </div>
                            <div class="flex items-center gap-2 bg-white/10 px-4 py-2.5 rounded-xl border border-white/10">
                                <svg class="w-4 h-4 text-orange-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
                                <span>تغليف حماية العفش</span>
                            </div>
                            <div class="flex items-center gap-2 bg-white/10 px-4 py-2.5 rounded-xl border border-white/10">
                                <svg class="w-4 h-4 text-orange-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                <span>معاينة مجانية</span>
                            </div>
                        </div>

                        <!-- CTA Buttons -->
                        <div class="flex flex-col sm:flex-row gap-4 sm:gap-6 justify-center lg:justify-start">
                            <a href="tel:+966500504024"
                                aria-label="اتصل الآن برقم شركة نقل عفش جدة نجوم العرب 0500504024"
                                class="bg-orange-500 hover:bg-orange-600 text-white font-bold px-8 py-3.5 rounded-full text-base sm:text-lg transition-colors flex items-center justify-center gap-3 shadow-xl">
                                <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" aria-hidden="true">
                                    <path
                                        d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1.003 1.003 0 011.02-.24c1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z" />
                                </svg>
                                <span>اتصل الآن: 0500504024</span>
                            </a>
                            <a href="https://wa.me/966500504024" target="_blank" rel="noopener noreferrer"
                                aria-label="تواصل عبر الواتساب مع شركة نجوم العرب"
                                class="bg-green-600 hover:bg-green-700 text-white font-bold px-8 py-3.5 rounded-full text-base sm:text-lg transition-colors flex items-center justify-center gap-3 shadow-xl">
                                <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" aria-hidden="true">
                                    <path
                                        d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.205 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z" />
                                </svg>
                                <span>مراسلة واتساب</span>
                            </a>
                        </div>
                    </div>

                    <!-- Real Hero Image Column (LCP Element) -->
                    <div class="flex-1 flex justify-center lg:justify-end w-full">
                        <div class="relative w-full max-w-md lg:max-w-xl">
                            <img src="/assets/img/hero-1200.webp"
                                srcset="/assets/img/hero-480.webp 480w, /assets/img/hero-768.webp 768w, /assets/img/hero-1200.webp 1200w"
                                sizes="(max-width: 768px) 100vw, 50vw"
                                alt="شركة نقل عفش جدة نجوم العرب — سيارة دينا مجهزة لنقل الأثاث"
                                width="1200" height="900"
                                fetchpriority="high" decoding="async"
                                class="w-full h-auto max-h-[440px] object-cover rounded-3xl bg-white/5 border border-white/10 shadow-2xl">
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- C. Trust Stats Section -->
        <section id="trust-stats" class="py-10 bg-white relative z-20 -mt-8 lg:-mt-12" aria-label="إحصائيات الثقة">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div
                    class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6 bg-white rounded-3xl shadow-xl p-6 md:p-8 border border-gray-100">
                    <div class="text-center">
                        <div class="text-3xl md:text-5xl font-extrabold text-orange-500 mb-1">+15</div>
                        <p class="text-gray-600 font-bold text-xs md:text-sm">سنوات خبرة في جدة</p>
                    </div>
                    <div class="text-center">
                        <div class="text-3xl md:text-5xl font-extrabold text-[#0a2540] mb-1">+1500</div>
                        <p class="text-gray-600 font-bold text-xs md:text-sm">عملية نقل ناجحة</p>
                    </div>
                    <div class="text-center">
                        <div class="text-3xl md:text-5xl font-extrabold text-orange-500 mb-1">+40</div>
                        <p class="text-gray-600 font-bold text-xs md:text-sm">سيارة نقل مجهزة</p>
                    </div>
                    <div class="text-center">
                        <div class="text-2xl md:text-4xl font-extrabold text-[#0a2540] mb-1">مجانية</div>
                        <p class="text-gray-600 font-bold text-xs md:text-sm">معاينة قبل الحجز</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- D. About Us Section -->
        <section id="about" class="py-16 bg-slate-50 border-b border-gray-100" aria-labelledby="about-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="flex flex-col lg:flex-row items-center justify-between gap-10 lg:gap-14">

                    <!-- Image Side -->
                    <div class="w-full lg:w-5/12 flex justify-center">
                        <img src="/assets/img/about.webp" alt="فريق عمل شركة نجوم العرب أثناء تغليف ونقل أثاث المنازل في جدة"
                            width="800" height="600" loading="lazy" decoding="async"
                            class="w-full max-w-md lg:max-w-full h-auto rounded-2xl border border-gray-200 shadow-md object-cover">
                    </div>

                    <!-- Content Side -->
                    <div class="w-full lg:w-7/12 text-right">
                        <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">من نحن وكيف نخدمك</span>

                        <h2 id="about-heading"
                            class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-[#0a2540] mb-4 leading-tight">
                            نجوم العرب: شركة نقل أثاث بجدة
                        </h2>

                        <p class="text-gray-700 leading-relaxed text-base sm:text-lg mb-4">
                            تُعد نجوم العرب شركة نقل عفش بجدة متخصصة في أعمال النقل السكني والمكتبي، حيث نمتلك أسطول سيارات دينا مجهز وخبرة تمتد لسنوات في نقل أثاث بجدة. نوفر حلولاً شاملة تشمل فك القطع الخشبية، التغليف بمواد واقية، والتركيب المتقن لضمان وصول مقتنياتك بسلام.
                        </p>

                        <p class="text-gray-700 leading-relaxed text-base sm:text-lg mb-6">
                            نقدم خدماتنا بمرونة لتغطية كافة أرجاء المدينة، مع إمكانية طلب <a
                                href="./furniture-packaging-in-jeddah/"
                                class="text-[#0a2540] font-semibold hover:text-orange-500 transition-colors">خدمات تغليف العفش</a> لحماية القطع القابلة للكسر، مستعينين بـ <a
                                href="./furniture-transport-trucks-in-jeddah/"
                                class="text-[#0a2540] font-semibold hover:text-orange-500 transition-colors">سيارات نقل العفش</a> المغلقة والمجهزة بالكامل، إلى جانب توفير <a
                                href="./furniture-lifting-crane-in-jeddah/"
                                class="text-[#0a2540] font-semibold hover:text-orange-500 transition-colors">ونش رفع عفش جدة</a> للأدوار العليا لتسهيل مهام النقل الصعبة.
                        </p>

                        <div
                            class="grid grid-cols-2 gap-3 text-xs sm:text-sm font-semibold text-[#0a2540] border-t border-gray-200 pt-4">
                            <div class="flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0" aria-hidden="true"></span>
                                <span>خدمات الفك والتركيب الاحترافي</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0" aria-hidden="true"></span>
                                <span>تغليف الأثاث بالكرتون والبابلز</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0" aria-hidden="true"></span>
                                <span>تحميل ونقل آمن داخل وخارج جدة</span>
                            </div>
                            <a href="./areas/"
                                class="flex items-center gap-2 text-[#0a2540] hover:text-orange-500 transition-colors">
                                <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0" aria-hidden="true"></span>
                                <span>تغطية شاملة لكل أحياء جدة</span>
                            </a>
                        </div>

                        <!-- CTA Buttons -->
                        <div class="flex flex-wrap items-center gap-4 mt-8 pt-2">
                            <a href="tel:+966500504024" aria-label="اتصل بشركة نجوم العرب لنقل الأثاث"
                                class="bg-orange-500 hover:bg-orange-600 text-white font-bold px-6 py-3 rounded-full text-sm sm:text-base transition-colors flex items-center gap-2 shadow-md">
                                <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1.003 1.003 0 011.02-.24c1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                                <span>اتصل بنا الآن</span>
                            </a>
                            <a href="https://wa.me/966500504024" target="_blank" rel="noopener noreferrer"
                                aria-label="تواصل عبر الواتساب مع نجوم العرب"
                                class="bg-green-600 hover:bg-green-700 text-white font-bold px-6 py-3 rounded-full text-sm sm:text-base transition-colors flex items-center gap-2 shadow-md">
                                <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.205 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                                <span>تواصل واتساب</span>
                            </a>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- E. Why We Are Reliable Section -->
        <section id="trust-details" class="py-16 bg-white border-b border-gray-100" aria-labelledby="trust-details-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="max-w-4xl mx-auto text-right">
                    <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">معايير الاحترافية والمصداقية</span>
                    <h2 id="trust-details-heading" class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-[#0a2540] mb-6">
                        لماذا نحن شركة نقل عفش موثوقة في جدة؟
                    </h2>

                    <div class="space-y-5 text-gray-700 leading-relaxed text-base sm:text-lg">
                        <p>
                            تعتمد موثوقيتنا في أعمال نقل العفش على تقديم باقة خدمات منظمة تتجاوز مجرد التحميل والتفريغ. إننا نتولى إدارة رحلة الانتقال كاملة عبر فحص أولي للمنقولات وتوفير مواد تغليف عالية الجودة كالبابلز والكرتون المضلع والشرائط اللاصقة، مما يجعل نقل أثاث بجدة تجربة مريحة ومحمية من التلف، سواء كنت تنتقل إلى شقة سكنية أو فيلا أو مقر شركة.
                        </p>
                        <p>
                            نتبع منهجية عمل دقيقة تبدأ بالتفكيك المنظم لغرف النوم والمطابخ والمكاتب بأيدي نجارين ماهرين، مروراً بتغليف كل قطعة وترقيم الصناديق لتسهيل فرزها، وانتهاءً برص الأثاث داخل سيارات النقل بنظام التثبيت المحكم لضمان استقرار الشحنة أثناء السير في مختلف شوارع وأحياء جدة.
                        </p>
                        <p>
                            نؤمن بأن الشفافية هي أساس التعامل السليم، ولذلك نلتزم بتقديم معاينة واضحة وتحديد الالتزامات قبل الانطلاق مع الحرص على سلامة المنقولات ومتابعة الإشراف المباشر حتى اكتمال التركيب والتسليم النهائي في المكان المحدد.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- F. Main Services Section (6 Cards) -->
        <section id="services" class="py-20 bg-gray-50 border-b border-gray-100" aria-labelledby="services-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="text-center mb-16">
                    <div class="inline-block">
                        <div class="flex items-center justify-center gap-2 mb-3">
                            <div class="w-8 h-px bg-orange-500" aria-hidden="true"></div>
                            <span class="text-orange-500 font-semibold text-lg tracking-wider">خدماتنا المتكاملة</span>
                            <div class="w-8 h-px bg-orange-500" aria-hidden="true"></div>
                        </div>
                    </div>
                    <h2 id="services-heading" class="text-3xl md:text-5xl font-bold text-[#0a2540] mt-4 mb-4">
                        خدمات نقل الأثاث في جدة
                    </h2>
                    <p class="text-gray-600 max-w-2xl mx-auto text-base sm:text-lg leading-relaxed">
                        نقدم حلولاً مدروسة لنقل الأثاث والعفش بأمان وسرعة، مدعومة بخدمات الفك والتركيب والتغليف المتين، مع أسطول سيارات دينا مجهزة وونش مخصص للأدوار المرتفعة.
                    </p>
                </div>

                <!-- 6 Service Cards -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <!-- Service Card 1: نقل عفش واختيار الشركة -->
                    <article
                        class="group relative bg-white rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 hover:-translate-y-1.5 overflow-hidden border border-gray-100 flex flex-col justify-between">
                        <div class="relative p-6 bg-slate-50 border-b border-gray-100">
                            <div class="w-16 h-16 flex justify-center items-center bg-white rounded-xl border border-gray-100 text-orange-500 mb-4">
                                <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M20 8h-3V4H1v13h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">نقل عفش وأثاث المنازل</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">
                                خدمات نقل متكاملة للشقق والفلل السكنية والمكاتب التجارية بجدة، مع فريق متمرس وسيارات مجهزة للمحافظة على العفش.
                            </p>
                        </div>
                        <div class="p-6 bg-white">
                            <a href="./best-furniture-moving-company-jeddah/"
                                class="inline-flex items-center gap-2 text-sm font-bold text-orange-500 hover:text-orange-600 transition-colors">
                                <span>دليل اختيار شركة نقل عفش</span>
                                <svg class="w-4 h-4 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </article>

                    <!-- Service Card 2: فك وتركيب الأثاث -->
                    <article
                        class="group relative bg-white rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 hover:-translate-y-1.5 overflow-hidden border border-gray-100 flex flex-col justify-between">
                        <div class="relative p-6 bg-slate-50 border-b border-gray-100">
                            <div class="w-16 h-16 flex justify-center items-center bg-white rounded-xl border border-gray-100 text-orange-500 mb-4">
                                <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M11 4a2 2 0 114 0v1a2 2 0 01-2 2 2 2 0 01-2-2V4zm2 6a2 2 0 012 2v7a2 2 0 01-2 2 2 2 0 01-2-2v-7a2 2 0 012-2z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">فك وتركيب الأثاث</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">
                                فك وتركيب غرف النوم، المطابخ، المكاتب، وأثاث ايكيا بأيدي نجارين متخصصين مع المحافظة على المفصلات والمسامير.
                            </p>
                        </div>
                        <div class="p-6 bg-white">
                            <a href="./furniture-disassembly-and-reassembly-in-jeddah/"
                                class="inline-flex items-center gap-2 text-sm font-bold text-orange-500 hover:text-orange-600 transition-colors">
                                <span>تفاصيل الفك والتركيب</span>
                                <svg class="w-4 h-4 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </article>

                    <!-- Service Card 3: تغليف العفش -->
                    <article
                        class="group relative bg-white rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 hover:-translate-y-1.5 overflow-hidden border border-gray-100 flex flex-col justify-between">
                        <div class="relative p-6 bg-slate-50 border-b border-gray-100">
                            <div class="w-16 h-16 flex justify-center items-center bg-white rounded-xl border border-gray-100 text-orange-500 mb-4">
                                <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">تغليف العفش الاحترافي</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">
                                حماية المنقولات باستخدام البابلز، الكرتون المضلع، والاسترتش لمنع الاحتكاك وتأمين القطع الزجاجية والأجهزة الحساسة.
                            </p>
                        </div>
                        <div class="p-6 bg-white">
                            <a href="./furniture-packaging-in-jeddah/"
                                class="inline-flex items-center gap-2 text-sm font-bold text-orange-500 hover:text-orange-600 transition-colors">
                                <span>خدمات تغليف الأثاث</span>
                                <svg class="w-4 h-4 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </article>

                    <!-- Service Card 4: سيارات النقل -->
                    <article
                        class="group relative bg-white rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 hover:-translate-y-1.5 overflow-hidden border border-gray-100 flex flex-col justify-between">
                        <div class="relative p-6 bg-slate-50 border-b border-gray-100">
                            <div class="w-16 h-16 flex justify-center items-center bg-white rounded-xl border border-gray-100 text-orange-500 mb-4">
                                <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M18 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm1.5-9l1.96 2.5H17V9.5h2.5zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM20 8h-3V4H1v13h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">سيارات دينا مجهزة</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">
                                شاحنات نقل مقفلة ومبطنة من الداخل بأحجام متعددة تناسب نقل الغرف الفردية والشقق الكبيرة بأمان كامل.
                            </p>
                        </div>
                        <div class="p-6 bg-white">
                            <a href="./furniture-transport-trucks-in-jeddah/"
                                class="inline-flex items-center gap-2 text-sm font-bold text-orange-500 hover:text-orange-600 transition-colors">
                                <span>أسطول شاحنات النقل</span>
                                <svg class="w-4 h-4 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </article>

                    <!-- Service Card 5: تخزين الأثاث -->
                    <article
                        class="group relative bg-white rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 hover:-translate-y-1.5 overflow-hidden border border-gray-100 flex flex-col justify-between">
                        <div class="relative p-6 bg-slate-50 border-b border-gray-100">
                            <div class="w-16 h-16 flex justify-center items-center bg-white rounded-xl border border-gray-100 text-orange-500 mb-4">
                                <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">تخزين الأثاث والعفش</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">
                                مستودعات مجهزة ومؤمنة لحفظ الأثاث والبضائع لفترات قصيرة أو طويلة مع عزل تام ضد الرطوبة والغبار.
                            </p>
                        </div>
                        <div class="p-6 bg-white">
                            <a href="./furniture-storage-in-jeddah/"
                                class="inline-flex items-center gap-2 text-sm font-bold text-orange-500 hover:text-orange-600 transition-colors">
                                <span>خدمات تخزين الأثاث</span>
                                <svg class="w-4 h-4 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </article>

                    <!-- Service Card 6: نقل بين المدن -->
                    <article
                        class="group relative bg-white rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 hover:-translate-y-1.5 overflow-hidden border border-gray-100 flex flex-col justify-between">
                        <div class="relative p-6 bg-slate-50 border-b border-gray-100">
                            <div class="w-16 h-16 flex justify-center items-center bg-white rounded-xl border border-gray-100 text-orange-500 mb-4">
                                <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">نقل العفش بين المدن</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">
                                رحلات نقل منتظمة من جدة إلى الرياض، مكة المكرمة، المدينة المنورة، الطائف، والدمام بشاحنات مقفلة وتثبيت محكم.
                            </p>
                        </div>
                        <div class="p-6 bg-white">
                            <a href="./intercity-moving/"
                                class="inline-flex items-center gap-2 text-sm font-bold text-orange-500 hover:text-orange-600 transition-colors">
                                <span>نقل العفش بين المدن</span>
                                <svg class="w-4 h-4 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <!-- G. Furniture Types & Property Types Section -->
        <section id="furniture-types" class="py-16 bg-slate-50 border-b border-gray-200">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">

                <!-- 1. Property Types Cards (Links to Targeted Landing Pages) -->
                <div class="mb-16 text-center">
                    <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">حلول مخصصة حسب نوع العقار</span>
                    <h2 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-[#0a2540] mb-4">
                        نقل عفش الشقق والفلل والمكاتب بجدة
                    </h2>
                    <p class="text-gray-600 max-w-3xl mx-auto text-base sm:text-lg mb-8 leading-relaxed">
                        نقدم خطط نقل متخصصة تلائم طبيعة العقار لضمان سهولة التحميل والتنزيل عبر المداخل والمصاعد والسلالم:
                    </p>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-right">
                        <!-- Apartments -->
                        <a href="./apartment-furniture-moving-jeddah/"
                            class="group block bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:shadow-md hover:border-orange-400 transition-all">
                            <div class="w-12 h-12 rounded-xl bg-orange-50 text-orange-500 flex items-center justify-center mb-4 group-hover:bg-orange-500 group-hover:text-white transition-colors">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] group-hover:text-orange-500 transition-colors mb-2">نقل عفش الشقق السكنية</h3>
                            <p class="text-gray-600 text-sm leading-relaxed mb-4">حلول سريعة لنقل أثاث الشقق بالأدوار المتعددة مع التغليف والتعامل مع الممرات الضيقة.</p>
                            <span class="text-xs font-bold text-orange-500 inline-flex items-center gap-1">عرض تفاصيل نقل الشقق ←</span>
                        </a>

                        <!-- Villas -->
                        <a href="./villa-moving-jeddah/"
                            class="group block bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:shadow-md hover:border-orange-400 transition-all">
                            <div class="w-12 h-12 rounded-xl bg-orange-50 text-orange-500 flex items-center justify-center mb-4 group-hover:bg-orange-500 group-hover:text-white transition-colors">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] group-hover:text-orange-500 transition-colors mb-2">نقل عفش الفلل والقصور</h3>
                            <p class="text-gray-600 text-sm leading-relaxed mb-4">طواقم متعددة وأسطول شاحنات لنقل المساحات الكبيرة والتحف والمجالس والحدائق بنظام دقيق.</p>
                            <span class="text-xs font-bold text-orange-500 inline-flex items-center gap-1">عرض تفاصيل نقل الفلل ←</span>
                        </a>

                        <!-- Offices -->
                        <a href="./office-furniture-moving-jeddah/"
                            class="group block bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:shadow-md hover:border-orange-400 transition-all">
                            <div class="w-12 h-12 rounded-xl bg-orange-50 text-orange-500 flex items-center justify-center mb-4 group-hover:bg-orange-500 group-hover:text-white transition-colors">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] group-hover:text-orange-500 transition-colors mb-2">نقل المكاتب والشركات</h3>
                            <p class="text-gray-600 text-sm leading-relaxed mb-4">نقل مكاتب العمل، الخزائن، الشاشات، وأجهزة الحاسب مع الحفاظ على سرعة التشغيل واستئناف العمل.</p>
                            <span class="text-xs font-bold text-orange-500 inline-flex items-center gap-1">عرض تفاصيل نقل المكاتب ←</span>
                        </a>
                    </div>
                </div>

                <!-- 2. Furniture Specific Items -->
                <div class="text-center">
                    <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">عناية متخصصة لكل قطعة</span>
                    <h2 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-[#0a2540] mb-4">
                        أنواع الأثاث التي ننقلها في جدة
                    </h2>
                    <p class="text-gray-600 max-w-3xl mx-auto text-base sm:text-lg mb-8 leading-relaxed">
                        نوفر خدمات نقل العفش المتخصصة لكافة أصناف الأثاث المنزلي والمكتبي مع تطبيق أساليب حماية مخصصة لكل نوع:
                    </p>

                    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4 text-right">
                        <a href="./ikea-furniture-moving-jeddah/" class="bg-white p-4 rounded-xl border border-gray-200 shadow-sm hover:border-orange-400 hover:shadow-md transition-all block">
                            <h3 class="font-bold text-[#0a2540] text-sm mb-1">غرف النوم وايكيا</h3>
                            <p class="text-gray-500 text-xs leading-relaxed">فك وتركيب الأسرة والدواليب ووحدات ايكيا.</p>
                        </a>
                        <a href="./kitchen-moving-jeddah/" class="bg-white p-4 rounded-xl border border-gray-200 shadow-sm hover:border-orange-400 hover:shadow-md transition-all block">
                            <h3 class="font-bold text-[#0a2540] text-sm mb-1">المطابخ والخزائن</h3>
                            <p class="text-gray-500 text-xs leading-relaxed">فك خزائن المطبخ والرخام وتغليفها.</p>
                        </a>
                        <a href="./ac-disassembly-and-moving-jeddah/" class="bg-white p-4 rounded-xl border border-gray-200 shadow-sm hover:border-orange-400 hover:shadow-md transition-all block">
                            <h3 class="font-bold text-[#0a2540] text-sm mb-1">فك ونقل المكيفات</h3>
                            <p class="text-gray-500 text-xs leading-relaxed">فك مكيفات سبليت وشباك وحبس الفريون.</p>
                        </a>
                        <div class="bg-white p-4 rounded-xl border border-gray-200 shadow-sm">
                            <h3 class="font-bold text-[#0a2540] text-sm mb-1">المجالس والكنب</h3>
                            <p class="text-gray-500 text-xs leading-relaxed">تغليف بالنايلون لحماية الأقمشة والجلد.</p>
                        </div>
                        <div class="bg-white p-4 rounded-xl border border-gray-200 shadow-sm">
                            <h3 class="font-bold text-[#0a2540] text-sm mb-1">الأجهزة والتحف</h3>
                            <p class="text-gray-500 text-xs leading-relaxed">صناديق مبطنة للشاشات والزجاج والتحف.</p>
                        </div>
                        <a href="./affordable-furniture-moving-jeddah/" class="bg-white p-4 rounded-xl border border-gray-200 shadow-sm hover:border-orange-400 hover:shadow-md transition-all block">
                            <h3 class="font-bold text-[#0a2540] text-sm mb-1">نقل أثاث اقتصادي</h3>
                            <p class="text-gray-500 text-xs leading-relaxed">خيارات مرنة بأسعار مناسبة لجميع الاحتياجات.</p>
                        </a>
                    </div>
                </div>

            </div>
        </section>

        <!-- H. Additional Specialized Services Section (6 Distinct Pages) -->
        <section id="additional-services" class="py-16 bg-white border-b border-gray-200" aria-labelledby="additional-services-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="text-center mb-12">
                    <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">خدمات متخصصة داعمة</span>
                    <h2 id="additional-services-heading" class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-[#0a2540] mb-4">
                        خدمات إضافية لنقل وتجهيز الأثاث بجدة
                    </h2>
                    <p class="text-gray-600 max-w-2xl mx-auto text-base sm:text-lg leading-relaxed">
                        نوفر باقة من الخدمات التخصصية التي يحتاجها عملاؤنا أثناء تجهيز وانتقال منازلهم في جدة:
                    </p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 text-right">
                    <!-- Service 1: Ikea -->
                    <article class="p-5 bg-slate-50 rounded-2xl border border-gray-100 hover:border-orange-300 transition-all">
                        <h3 class="text-lg font-bold text-[#0a2540] mb-2">
                            <a href="./ikea-furniture-moving-jeddah/" class="hover:text-orange-500 transition-colors">فك وتركيب ونقل أثاث ايكيا بجدة</a>
                        </h3>
                        <p class="text-gray-600 text-sm leading-relaxed mb-3">
                            خدمة متخصصة لفك ونقل دواليب باكس PAX، غرف النوم، ووحدات بيستا وكالاكس بعناية تامة دون خدوش.
                        </p>
                        <a href="./ikea-furniture-moving-jeddah/" class="text-xs font-bold text-orange-500 hover:underline">تفاصيل نقل أثاث ايكيا ←</a>
                    </article>

                    <!-- Service 2: Kitchens -->
                    <article class="p-5 bg-slate-50 rounded-2xl border border-gray-100 hover:border-orange-300 transition-all">
                        <h3 class="text-lg font-bold text-[#0a2540] mb-2">
                            <a href="./kitchen-moving-jeddah/" class="hover:text-orange-500 transition-colors">نقل مطابخ بجدة</a>
                        </h3>
                        <p class="text-gray-600 text-sm leading-relaxed mb-3">
                            فك وتغليف خزائن المطبخ، الأسطح الرخامية، وتأمين الأجهزة والأبواب الزجاجية قبل إعادة التركيب.
                        </p>
                        <a href="./kitchen-moving-jeddah/" class="text-xs font-bold text-orange-500 hover:underline">تفاصيل نقل المطابخ ←</a>
                    </article>

                    <!-- Service 3: AC Disassembly -->
                    <article class="p-5 bg-slate-50 rounded-2xl border border-gray-100 hover:border-orange-300 transition-all">
                        <h3 class="text-lg font-bold text-[#0a2540] mb-2">
                            <a href="./ac-disassembly-and-moving-jeddah/" class="hover:text-orange-500 transition-colors">فك وتركيب ونقل المكيفات بجدة</a>
                        </h3>
                        <p class="text-gray-600 text-sm leading-relaxed mb-3">
                            فك ونقل مكيفات سبليت وشباك بواسطة فنيين متخصصين مع الحفاظ على الفريون وتأمين التمديدات.
                        </p>
                        <a href="./ac-disassembly-and-moving-jeddah/" class="text-xs font-bold text-orange-500 hover:underline">تفاصيل نقل المكيفات ←</a>
                    </article>

                    <!-- Service 4: Old Furniture Removal -->
                    <article class="p-5 bg-slate-50 rounded-2xl border border-gray-100 hover:border-orange-300 transition-all">
                        <h3 class="text-lg font-bold text-[#0a2540] mb-2">
                            <a href="./old-furniture-removal-jeddah/" class="hover:text-orange-500 transition-colors">التخلص من الأثاث القديم والرجيع بجدة</a>
                        </h3>
                        <p class="text-gray-600 text-sm leading-relaxed mb-3">
                            إزالة العفش التالف والكنب والمراتب وتفريغ الشقق والعمائر بطرق نظامية معتمدة دون رميها بالشارع.
                        </p>
                        <a href="./old-furniture-removal-jeddah/" class="text-xs font-bold text-orange-500 hover:underline">تفاصيل إزالة العفش القديم ←</a>
                    </article>

                    <!-- Service 5: Small Truck -->
                    <article class="p-5 bg-slate-50 rounded-2xl border border-gray-100 hover:border-orange-300 transition-all">
                        <h3 class="text-lg font-bold text-[#0a2540] mb-2">
                            <a href="./small-moving-truck-jeddah/" class="hover:text-orange-500 transition-colors">ونيت نقل عفش ودينا صغيرة بجدة</a>
                        </h3>
                        <p class="text-gray-600 text-sm leading-relaxed mb-3">
                            دينا صغيرة وونيت للمشاوير السريعة ونقل القطع المفردة وسكن العزاب والطلاب بأسعار مناسبة.
                        </p>
                        <a href="./small-moving-truck-jeddah/" class="text-xs font-bold text-orange-500 hover:underline">تفاصيل الونيت والدينا الصغيرة ←</a>
                    </article>

                    <!-- Service 6: Filipino Labour -->
                    <article class="p-5 bg-slate-50 rounded-2xl border border-gray-100 hover:border-orange-300 transition-all">
                        <h3 class="text-lg font-bold text-[#0a2540] mb-2">
                            <a href="./filipino-moving-labour-jeddah/" class="hover:text-orange-500 transition-colors">شركة نقل عفش عمالة فلبينية بجدة</a>
                        </h3>
                        <p class="text-gray-600 text-sm leading-relaxed mb-3">
                            توفير طواقم عمالة فلبينية وفنية مدربة لنقل وتغليف أثاث الشقق والفلل بهدوء ودقة متناهية.
                        </p>
                        <a href="./filipino-moving-labour-jeddah/" class="text-xs font-bold text-orange-500 hover:underline">تفاصيل العمالة الفلبينية ←</a>
                    </article>
                </div>
            </div>
        </section>

        <!-- I. Moving Process (6 Steps) -->
        <section id="moving-process" class="py-16 bg-white border-b border-gray-200" aria-labelledby="process-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="text-center mb-16">
                    <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">خطوات منظمة لنقل آمن</span>
                    <h2 id="process-heading" class="text-3xl md:text-4xl font-extrabold text-[#0a2540] mb-4">
                        مراحل نقل العفش والأثاث في جدة
                    </h2>
                    <p class="text-gray-600 max-w-2xl mx-auto text-base sm:text-lg leading-relaxed">
                        نتبع خطة عمل واضحة تضمن سلامة أثاثك وتوفر وقتك من أول اتصال وحتى استقرارك في المكان الجديد:
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 text-right">
                    <!-- Step 1 -->
                    <div class="bg-slate-50 p-6 rounded-2xl border border-gray-100 flex gap-4 items-start">
                        <span class="w-10 h-10 rounded-full bg-orange-500 text-white font-extrabold flex items-center justify-center shrink-0 text-lg">1</span>
                        <div>
                            <h3 class="text-lg font-bold text-[#0a2540] mb-2">التواصل والمعاينة</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">استقبال طلبك وتحديد حجم العفش والموقع والأدوار وتحديد موعد المعاينة المجانية.</p>
                        </div>
                    </div>

                    <!-- Step 2 -->
                    <div class="bg-slate-50 p-6 rounded-2xl border border-gray-100 flex gap-4 items-start">
                        <span class="w-10 h-10 rounded-full bg-orange-500 text-white font-extrabold flex items-center justify-center shrink-0 text-lg">2</span>
                        <div>
                            <h3 class="text-lg font-bold text-[#0a2540] mb-2">الفك المتخصص</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">فك غرف النوم والمطابخ والمكيفات بأيدي نجارين وفنيين مع ترقيم المسامير والقطع.</p>
                        </div>
                    </div>

                    <!-- Step 3 -->
                    <div class="bg-slate-50 p-6 rounded-2xl border border-gray-100 flex gap-4 items-start">
                        <span class="w-10 h-10 rounded-full bg-orange-500 text-white font-extrabold flex items-center justify-center shrink-0 text-lg">3</span>
                        <div>
                            <h3 class="text-lg font-bold text-[#0a2540] mb-2">التغليف الشامل</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">استخدام البابلز والكرتون المقوى والاسترتش لحماية كل قطعة وتأمين التحف والزجاج.</p>
                        </div>
                    </div>

                    <!-- Step 4 -->
                    <div class="bg-slate-50 p-6 rounded-2xl border border-gray-100 flex gap-4 items-start">
                        <span class="w-10 h-10 rounded-full bg-orange-500 text-white font-extrabold flex items-center justify-center shrink-0 text-lg">4</span>
                        <div>
                            <h3 class="text-lg font-bold text-[#0a2540] mb-2">التحميل والتنزيل</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">تنزيل الأثاث بحرص عبر المصاعد أو السلالم أو الونش الهيدروليكي للأدوار المرتفعة.</p>
                        </div>
                    </div>

                    <!-- Step 5 -->
                    <div class="bg-slate-50 p-6 rounded-2xl border border-gray-100 flex gap-4 items-start">
                        <span class="w-10 h-10 rounded-full bg-orange-500 text-white font-extrabold flex items-center justify-center shrink-0 text-lg">5</span>
                        <div>
                            <h3 class="text-lg font-bold text-[#0a2540] mb-2">النقل بسيارات مجهزة</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">رص العفش وتثبيته داخل شاحنات مقفلة وسائقين ذوي دراية بمسارات وشوارع جدة.</p>
                        </div>
                    </div>

                    <!-- Step 6 -->
                    <div class="bg-slate-50 p-6 rounded-2xl border border-gray-100 flex gap-4 items-start">
                        <span class="w-10 h-10 rounded-full bg-orange-500 text-white font-extrabold flex items-center justify-center shrink-0 text-lg">6</span>
                        <div>
                            <h3 class="text-lg font-bold text-[#0a2540] mb-2">التركيب والتسليم</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">إعادة تركيب الأثاث وترتيب الغرف في موقعك الجديد حسب رغبتك والتأكد من رضاك التام.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- J & K. Pricing Factors & Pricing Tables Section -->
        <section id="pricing-section" class="py-16 bg-slate-50 border-b border-gray-200" aria-labelledby="pricing-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="text-center mb-12">
                    <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">شفافية وتكلفة عادلة</span>
                    <h2 id="pricing-heading" class="text-3xl md:text-4xl font-extrabold text-[#0a2540] mb-4">
                        أسعار نقل العفش بجدة
                    </h2>
                    <p class="text-gray-600 max-w-3xl mx-auto text-base sm:text-lg leading-relaxed">
                        تتحدد تكلفة نقل العفش في جدة وفق عوامل واضحة تشمل حجم المنقولات، عدد الغرف، مسافة الانتقال، والخدمات الإضافية كالفك والتغليف أو الونش. تفضل بالاطلاع على التفاصيل الكاملة في <a href="./furniture-moving-prices-jeddah/" class="font-bold text-orange-500 hover:underline">دليل أسعار نقل العفش بجدة</a>، وفيما يلي أهم العوامل وجدول تقديري:
                    </p>
                </div>

                <!-- J. 9 Pricing Factors (1 concise line each) -->
                <div class="bg-white rounded-2xl p-6 border border-gray-200 shadow-sm max-w-4xl mx-auto mb-10 text-right">
                    <h3 class="text-lg font-bold text-[#0a2540] mb-4 border-b pb-2">9 عوامل أساسية تحدد سعر نقل العفش:</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs sm:text-sm text-gray-700">
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0"></span>
                            <span><strong>حجم المنقولات:</strong> عدد الغرف وكمية الصناديق والمفروشات.</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0"></span>
                            <span><strong>نوع وحجم الشاحنة:</strong> دينا مقفلة كبيرة أو ونيت لمشوار سريع.</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0"></span>
                            <span><strong>المسافة المقطوعة:</strong> النقل بين أحياء جدة أو بين المدن.</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0"></span>
                            <span><strong>أدوار المبنى والمصعد:</strong> توفر مصعد واسع أو الاعتماد على الدرج.</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0"></span>
                            <span><strong>خدمات الفك والتركيب:</strong> فك غرف النوم والمطابخ والمكاتب.</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0"></span>
                            <span><strong>مواد التغليف:</strong> كمية الكرتون والبابلز والاسترتش المستخدمة.</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0"></span>
                            <span><strong>استخدام ونش الرفع:</strong> ونش هيدروليكي للأدوار المرتفعة.</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0"></span>
                            <span><strong>فك ونقل المكيفات:</strong> فني تبريد لفك وتركيب وحدات السبليت.</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-orange-500 flex-shrink-0"></span>
                            <span><strong>القطع الخاصة:</strong> فني متخصص لقطع ايكيا المعقدة والزجاج.</span>
                        </div>
                    </div>
                </div>

                <!-- K. Pricing Tables -->
                <div class="bg-white rounded-2xl p-6 border border-gray-200 shadow-sm max-w-4xl mx-auto text-right">
                    <h3 class="text-xl font-bold text-[#0a2540] mb-2 text-center">جدول تقديري لتكلفة نقل العفش داخل وخارج جدة</h3>
                    <p class="text-gray-500 text-xs text-center mb-6 leading-relaxed">
                        الأسعار تقديرية وتتحدد بدقة بعد المعاينة الفعلية أو تزويدنا بتفاصيل المنقولات هاتفياً.
                    </p>

                    <!-- Table 1: Residential Moving by Size -->
                    <div class="overflow-x-auto mb-8">
                        <table class="w-full text-sm text-right text-gray-700 bg-white rounded-xl overflow-hidden border border-gray-200">
                            <thead class="bg-[#0a2540] text-white text-xs uppercase">
                                <tr>
                                    <th scope="col" class="px-4 py-3">حجم السكن والمنقولات</th>
                                    <th scope="col" class="px-4 py-3">نطاق التغطية</th>
                                    <th scope="col" class="px-4 py-3">الخدمات الأساسية</th>
                                    <th scope="col" class="px-4 py-3">نطاق السعر التقديري</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-200">
                                <tr class="hover:bg-gray-50">
                                    <td class="px-4 py-3 font-semibold text-[#0a2540]">استوديو / غرفة وصالة</td>
                                    <td class="px-4 py-3">داخل أحياء جدة</td>
                                    <td class="px-4 py-3">دينا نقل + عمالة تحميل وتنزيل</td>
                                    <td class="px-4 py-3 font-bold text-orange-600">350 – 500 ريال</td>
                                </tr>
                                <tr class="hover:bg-gray-50">
                                    <td class="px-4 py-3 font-semibold text-[#0a2540]">شقة غرفتين وصالة</td>
                                    <td class="px-4 py-3">داخل أحياء جدة</td>
                                    <td class="px-4 py-3">دينا مجهزة + عمالة نقل وتحميل</td>
                                    <td class="px-4 py-3 font-bold text-orange-600">600 – 800 ريال</td>
                                </tr>
                                <tr class="hover:bg-gray-50">
                                    <td class="px-4 py-3 font-semibold text-[#0a2540]">شقة 3 غرف وصالة</td>
                                    <td class="px-4 py-3">داخل أحياء جدة</td>
                                    <td class="px-4 py-3">دينا كبيرة + طاقم عمالة متخصص</td>
                                    <td class="px-4 py-3 font-bold text-orange-600">850 – 1100 ريال</td>
                                </tr>
                                <tr class="hover:bg-gray-50">
                                    <td class="px-4 py-3 font-semibold text-[#0a2540]">شقة 4 إلى 5 غرف</td>
                                    <td class="px-4 py-3">داخل أحياء جدة</td>
                                    <td class="px-4 py-3">شاحنتان أو دينا رحلتين + فريق عمل كامل</td>
                                    <td class="px-4 py-3 font-bold text-orange-600">1200 – 1600 ريال</td>
                                </tr>
                                <tr class="hover:bg-gray-50">
                                    <td class="px-4 py-3 font-semibold text-[#0a2540]">فيلا كاملة / دور مستقل</td>
                                    <td class="px-4 py-3">داخل أحياء جدة</td>
                                    <td class="px-4 py-3">أسطول شاحنات + فريق عمل متكامل</td>
                                    <td class="px-4 py-3 font-bold text-orange-600">1800 – 2800 ريال</td>
                                </tr>
                                <tr class="hover:bg-gray-50 bg-orange-50/50">
                                    <td class="px-4 py-3 font-semibold text-[#0a2540]">نقل بين المدن (الرياض، مكة، المدينة...)</td>
                                    <td class="px-4 py-3">من جدة لباقي المدن</td>
                                    <td class="px-4 py-3">شاحنة مغلقة مجهزة للمسافات الطويلة</td>
                                    <td class="px-4 py-3 font-bold text-orange-600">حسب المسافة والمدينة</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- Table 2: Add-on Services -->
                    <h4 class="text-base font-bold text-[#0a2540] mb-3">الخدمات الإضافية والمساندة (اختياري حسب الطلب):</h4>
                    <div class="overflow-x-auto mb-6">
                        <table class="w-full text-sm text-right text-gray-700 bg-white rounded-xl overflow-hidden border border-gray-200">
                            <thead class="bg-gray-100 text-[#0a2540] text-xs">
                                <tr>
                                    <th scope="col" class="px-4 py-2.5">الخدمة الإضافية</th>
                                    <th scope="col" class="px-4 py-2.5">الوصف والتفاصيل</th>
                                    <th scope="col" class="px-4 py-2.5">التكلفة التقديرية</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-200 text-xs sm:text-sm">
                                <tr>
                                    <td class="px-4 py-2.5 font-semibold">أدوار مرتفعة بدون مصعد (دور 2 إلى 4)</td>
                                    <td class="px-4 py-2.5">مجهود بدني إضافي لتنزيل ورفع القطع عبر الدرج</td>
                                    <td class="px-4 py-2.5 font-bold text-gray-800">+150 ريال</td>
                                </tr>
                                <tr>
                                    <td class="px-4 py-2.5 font-semibold">أدوار مرتفعة بدون مصعد (دور 5 فأعلى)</td>
                                    <td class="px-4 py-2.5">إنزال ورفع يدوي لأدوار شاهقة دون مصعد</td>
                                    <td class="px-4 py-2.5 font-bold text-gray-800">+300 ريال</td>
                                </tr>
                                <tr>
                                    <td class="px-4 py-2.5 font-semibold">ونش رفع عفش هيدروليكي</td>
                                    <td class="px-4 py-2.5">رفع وتنزيل الأثاث عبر النوافذ والواجهات للأدوار العليا</td>
                                    <td class="px-4 py-2.5 font-bold text-gray-800">+450 ريال</td>
                                </tr>
                                <tr>
                                    <td class="px-4 py-2.5 font-semibold">تغليف وقائي بالبابلز والكرتون</td>
                                    <td class="px-4 py-2.5">تغليف الصالونات وغرف النوم والقطع الحساسة بالكامل</td>
                                    <td class="px-4 py-2.5 font-bold text-gray-800">+150 ريال</td>
                                </tr>
                                <tr>
                                    <td class="px-4 py-2.5 font-semibold">فك وتركيب مكيفات سبليت</td>
                                    <td class="px-4 py-2.5">بواسطة فني تكييف مع حبس الفريون وتأمين الوحدة</td>
                                    <td class="px-4 py-2.5 font-bold text-gray-800">+150 ريال / للمكيف</td>
                                </tr>
                                <tr>
                                    <td class="px-4 py-2.5 font-semibold">فني تركيب قطع وأثاث ايكيا</td>
                                    <td class="px-4 py-2.5">نجار خبير في تفكيك وتركيب غرف ودواليب ايكيا المعقدة</td>
                                    <td class="px-4 py-2.5 font-bold text-gray-800">+100 ريال</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="p-4 bg-orange-50 rounded-xl border border-orange-200 text-center">
                        <p class="text-xs sm:text-sm text-gray-700 leading-relaxed mb-3">
                            هل ترغب في معرفة التكلفة الدقيقة لنقل عفشك؟ فريقنا يقدم خدمة <strong>المعاينة المجانية</strong> داخل جدة.
                        </p>
                        <div class="flex flex-wrap justify-center gap-3">
                            <a href="./furniture-moving-prices-jeddah/"
                                class="bg-[#0a2540] hover:bg-[#081d33] text-white text-xs sm:text-sm font-bold px-5 py-2.5 rounded-full transition-colors">
                                استعراض دليل أسعار نقل العفش بجدة
                            </a>
                            <a href="tel:+966500504024"
                                class="bg-orange-500 hover:bg-orange-600 text-white text-xs sm:text-sm font-bold px-5 py-2.5 rounded-full transition-colors">
                                احجز موعد معاينة مجانية
                            </a>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <!-- L. Districts / Areas Section (All 10 Live Neighborhoods) -->
        <section id="jeddah-districts" class="py-16 bg-white border-b border-gray-200" aria-labelledby="districts-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="text-center mb-12">
                    <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">تغطية جغرافية كاملة</span>
                    <h2 id="districts-heading" class="text-3xl md:text-4xl font-extrabold text-[#0a2540] mb-4">
                        نقل عفش داخل أحياء جدة
                    </h2>
                    <p class="text-gray-600 max-w-3xl mx-auto text-base sm:text-lg leading-relaxed">
                        نغطي كافة أحياء ومربعات عروس البحر الأحمر بسيارات نقل مجهزة وطواقم متواجدة بالقرب منك لتلبية طلبك في أسرع وقت.
                    </p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 text-right mb-10">
                    <!-- شمال جدة -->
                    <article class="bg-slate-50 p-5 rounded-2xl border border-gray-200 shadow-sm">
                        <h3 class="font-bold text-[#0a2540] text-lg mb-3 border-b pb-2">نقل عفش شمال جدة</h3>
                        <ul class="text-gray-600 text-sm space-y-2.5 leading-relaxed">
                            <li><a href="./areas/furniture-moving-in-hayu-alshati-jeddah/" class="hover:text-orange-500 font-medium">نقل عفش حي الشاطئ</a></li>
                            <li><a href="./areas/furniture-moving-obhur-alshamaliyah/" class="hover:text-orange-500 font-medium">نقل عفش أبحر الشمالية</a></li>
                            <li><a href="./areas/furniture-moving-hayu-alnaeem/" class="hover:text-orange-500 font-medium">نقل عفش حي النعيم</a></li>
                            <li><a href="./areas/furniture-moving-hayu-alhamdaniyah/" class="hover:text-orange-500 font-medium">نقل عفش حي الحمدانية</a></li>
                        </ul>
                    </article>

                    <!-- غرب ووسط جدة -->
                    <article class="bg-slate-50 p-5 rounded-2xl border border-gray-200 shadow-sm">
                        <h3 class="font-bold text-[#0a2540] text-lg mb-3 border-b pb-2">نقل عفش غرب ووسط جدة</h3>
                        <ul class="text-gray-600 text-sm space-y-2.5 leading-relaxed">
                            <li><a href="./areas/furniture-moving-hayu-alrawdah/" class="hover:text-orange-500 font-medium">نقل عفش حي الروضة</a></li>
                            <li><a href="./areas/furniture-moving-hayu-alzahra/" class="hover:text-orange-500 font-medium">نقل عفش حي الزهراء</a></li>
                            <li><a href="./areas/furniture-moving-hayu-alsalama/" class="hover:text-orange-500 font-medium">نقل عفش حي السلامة</a></li>
                            <li><a href="./areas/hayu-alhamra/" class="hover:text-orange-500 font-medium">نقل عفش حي الحمراء</a></li>
                        </ul>
                    </article>

                    <!-- شرق وجنوب جدة -->
                    <article class="bg-slate-50 p-5 rounded-2xl border border-gray-200 shadow-sm">
                        <h3 class="font-bold text-[#0a2540] text-lg mb-3 border-b pb-2">نقل عفش شرق جدة</h3>
                        <ul class="text-gray-600 text-sm space-y-2.5 leading-relaxed">
                            <li><a href="./areas/furniture-moving-hayu-al-safa/" class="hover:text-orange-500 font-medium">نقل عفش حي الصفا</a></li>
                            <li><a href="./areas/hayu-almarwah/" class="hover:text-orange-500 font-medium">نقل عفش حي المروة</a></li>
                        </ul>
                    </article>

                    <!-- دليل الأحياء الشامل -->
                    <article class="bg-orange-50/60 p-5 rounded-2xl border border-orange-200 shadow-sm flex flex-col justify-between">
                        <div>
                            <h3 class="font-bold text-[#0a2540] text-lg mb-3 border-b border-orange-200 pb-2">تغطية كافة الأحياء</h3>
                            <p class="text-gray-700 text-xs sm:text-sm leading-relaxed mb-4">
                                سياراتنا وطواقمنا تجوب مختلف أحياء ومخططات جدة يومياً لخدمتك أينما كنت.
                            </p>
                        </div>
                        <a href="./areas/"
                            class="inline-block bg-[#0a2540] hover:bg-[#081d33] text-white text-xs sm:text-sm font-bold px-4 py-2.5 rounded-xl text-center transition-colors">
                            استكشف جميع أحياء جدة ←
                        </a>
                    </article>
                </div>
            </div>
        </section>

        <!-- M. Disassembly & Packaging Deep Dive -->
        <section id="disassembly-section" class="py-20 bg-gradient-to-b from-gray-50 to-white border-b border-gray-200">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="flex flex-col lg:flex-row items-center justify-between gap-12">
                    <div class="w-full lg:w-1/2 text-right">
                        <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">حرفية وفك دقيق</span>
                        <h2 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-[#0a2540] mb-6">
                            فك وتركيب غرف النوم والمطابخ بجدة
                        </h2>
                        <p class="text-gray-700 leading-relaxed text-base sm:text-lg mb-6">
                            تتطلب قطع الأثاث الكبيرة دقة فائقة عند فكها لتجنب تلف المفصلات أو تشقق الخشب. يعتمد فريقنا على فنيين متخصصين في <a href="./furniture-disassembly-and-reassembly-in-jeddah/" class="font-bold text-[#0a2540] hover:text-orange-500 transition-colors">فك وتركيب وتغليف العفش بجدة</a>، كما نوفر <a href="./carpenter-furniture-disassembly-assembly-jeddah/" class="font-bold text-orange-500 hover:underline">نجار فك وتركيب غرف نوم بجدة</a> مجهزاً بالأدوات الحديثة للتعامل مع خزائن الملابس، غرف النوم الرئيسية، أثاث ايكيا، ومطابخ الألمنيوم والخشب باحترافية كاملة.
                        </p>
                        <div class="grid grid-cols-2 gap-4 text-sm text-gray-700 font-medium">
                            <div class="flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-orange-500"></span>
                                <span>ترقيم القطع والمسامير</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-orange-500"></span>
                                <span>إعادة تجميع متطابقة</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-orange-500"></span>
                                <span>حماية الزوايا والمفصلات</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-orange-500"></span>
                                <span>أدوات فك متطورة</span>
                            </div>
                        </div>
                    </div>
                    <div class="w-full lg:w-1/2 flex justify-center">
                        <img src="/assets/img/furniture-disassembly-jeddah-3.webp"
                            srcset="/assets/img/furniture-disassembly-jeddah-3-480.webp 480w, /assets/img/furniture-disassembly-jeddah-3.webp 800w"
                            sizes="(max-width: 768px) 100vw, 50vw"
                            alt="نجار متخصص أثناء فك وتركيب غرف النوم بجدة"
                            width="800" height="600" loading="lazy" decoding="async"
                            class="w-full max-w-lg rounded-2xl shadow-lg border border-gray-200 object-cover">
                    </div>
                </div>
            </div>
        </section>

        <!-- Packaging Deep Dive -->
        <section id="packaging-section" class="py-20 bg-white border-b border-gray-200">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="flex flex-col lg:flex-row-reverse items-center justify-between gap-12">
                    <div class="w-full lg:w-1/2 text-right">
                        <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">حماية قصوى لمقتنياتك</span>
                        <h2 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-[#0a2540] mb-6">
                            تغليف العفش بأجود الخامات المانعة للصدمات
                        </h2>
                        <p class="text-gray-700 leading-relaxed text-base sm:text-lg mb-6">
                            يعتبر التغليف الجيد هو خط الدفاع الأول لمنع الخدوش والكسر أثناء الرفع والتحميل والتنزيل. نحرص على استخدام خامات متعددة تناسب كل قطعة: البابلز الفقاعي للقطع الزجاجية والتحف، الكرتون المقوى للشاشات والأجهزة، والنايلون الاسترتش لحماية أقمشة الكنب والمفروشات من الغبار والرطوبة.
                        </p>
                        <div class="flex flex-wrap gap-3">
                            <span class="bg-slate-100 text-[#0a2540] px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold">بابلز فقاعي سميك</span>
                            <span class="bg-slate-100 text-[#0a2540] px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold">كرتون مضلع 5 طبقات</span>
                            <span class="bg-slate-100 text-[#0a2540] px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold">نايلون استرتش مطاطي</span>
                            <span class="bg-slate-100 text-[#0a2540] px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold">أشرطة تثبيت مقواة</span>
                        </div>
                    </div>
                    <div class="w-full lg:w-1/2 flex justify-center">
                        <img src="/assets/img/furniture-packaging-jeddah-1.webp"
                            srcset="/assets/img/furniture-packaging-jeddah-1-480.webp 480w, /assets/img/furniture-packaging-jeddah-1.webp 800w"
                            sizes="(max-width: 768px) 100vw, 50vw"
                            alt="عمليات تغليف الأثاث بالكرتون والبابلز في جدة"
                            width="800" height="600" loading="lazy" decoding="async"
                            class="w-full max-w-lg rounded-2xl shadow-lg border border-gray-200 object-cover">
                    </div>
                </div>
            </div>
        </section>

        <!-- N. Gallery / Portfolio Section (6 Real Work Photos) -->
        <section id="portfolio" class="py-20 bg-slate-50 border-b border-gray-200" aria-labelledby="portfolio-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="text-center mb-16">
                    <span class="text-orange-500 font-bold text-lg tracking-wider">معرض أعمالنا الميدانية</span>
                    <h2 id="portfolio-heading" class="text-3xl md:text-4xl font-extrabold text-[#0a2540] mt-3 mb-4">
                        صور واقعية لعمليات نقل وتغليف العفش بجدة
                    </h2>
                    <p class="text-gray-600 max-w-2xl mx-auto text-base sm:text-lg">
                        نوثق جانباً من الأعمال اليومية لفريقنا في فك، تغليف، وتحميل الأثاث بمختلف أحياء جدة.
                    </p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    <!-- Photo 1 -->
                    <div class="group relative rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 bg-white border border-gray-200">
                        <img src="/assets/img/furniture-packaging-jeddah-1.webp"
                            srcset="/assets/img/furniture-packaging-jeddah-1-480.webp 480w, /assets/img/furniture-packaging-jeddah-1.webp 800w"
                            sizes="(max-width: 768px) 100vw, 33vw"
                            alt="تغليف وتجهيز الأثاث بالكرتون المقوى والبابلز"
                            width="800" height="600" loading="lazy" decoding="async"
                            class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
                        <div class="p-4 bg-white text-right">
                            <h3 class="font-bold text-[#0a2540] text-base">تغليف وتجهيز الأثاث</h3>
                            <p class="text-gray-500 text-xs">حماية القطع الخشبية والأسطح بالكرتون والبابلز.</p>
                        </div>
                    </div>

                    <!-- Photo 2 -->
                    <div class="group relative rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 bg-white border border-gray-200">
                        <img src="/assets/img/furniture-moving-truck-jeddah-2.webp"
                            srcset="/assets/img/furniture-moving-truck-jeddah-2-480.webp 480w, /assets/img/furniture-moving-truck-jeddah-2.webp 800w"
                            sizes="(max-width: 768px) 100vw, 33vw"
                            alt="سيارات دينا نقل عفش مجهزة ومقفلة في شوارع جدة"
                            width="800" height="600" loading="lazy" decoding="async"
                            class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
                        <div class="p-4 bg-white text-right">
                            <h3 class="font-bold text-[#0a2540] text-base">سيارات نقل عفش مجهزة</h3>
                            <p class="text-gray-500 text-xs">شاحنات دينا مقفلة مخصصة لحماية المنقولات.</p>
                        </div>
                    </div>

                    <!-- Photo 3 -->
                    <div class="group relative rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 bg-white border border-gray-200">
                        <img src="/assets/img/furniture-disassembly-jeddah-3.webp"
                            srcset="/assets/img/furniture-disassembly-jeddah-3-480.webp 480w, /assets/img/furniture-disassembly-jeddah-3.webp 800w"
                            sizes="(max-width: 768px) 100vw, 33vw"
                            alt="نجار يفك الدواليب والقطع الخشبية الكبيرة بحرفية"
                            width="800" height="600" loading="lazy" decoding="async"
                            class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
                        <div class="p-4 bg-white text-right">
                            <h3 class="font-bold text-[#0a2540] text-base">فك غرف النوم والقطع الخشبية</h3>
                            <p class="text-gray-500 text-xs">تفكيك دقيق مع ترقيم المسامير والقطع لتسهيل التركيب.</p>
                        </div>
                    </div>

                    <!-- Photo 4 -->
                    <div class="group relative rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 bg-white border border-gray-200">
                        <img src="/assets/img/furniture-loading-jeddah-4.webp"
                            srcset="/assets/img/furniture-loading-jeddah-4-480.webp 480w, /assets/img/furniture-loading-jeddah-4.webp 800w"
                            sizes="(max-width: 768px) 100vw, 33vw"
                            alt="ترتيب وتثبيت قطع الأثاث داخل صندوق الشاحنة"
                            width="800" height="600" loading="lazy" decoding="async"
                            class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
                        <div class="p-4 bg-white text-right">
                            <h3 class="font-bold text-[#0a2540] text-base">ترتيب وتحميل العفش بالسيارة</h3>
                            <p class="text-gray-500 text-xs">رص احترافي مع أحزمة تثبيت تمنع الاهتزاز أثناء السير.</p>
                        </div>
                    </div>

                    <!-- Photo 5 -->
                    <div class="group relative rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 bg-white border border-gray-200">
                        <img src="/assets/img/fragile-items-protection-jeddah-5.webp"
                            srcset="/assets/img/fragile-items-protection-jeddah-5-480.webp 480w, /assets/img/fragile-items-protection-jeddah-5.webp 800w"
                            sizes="(max-width: 768px) 100vw, 33vw"
                            alt="تغليف الشاشات والزجاج بطبقات الحماية الإضافية"
                            width="800" height="600" loading="lazy" decoding="async"
                            class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
                        <div class="p-4 bg-white text-right">
                            <h3 class="font-bold text-[#0a2540] text-base">حماية الزجاج والأجهزة الحساسة</h3>
                            <p class="text-gray-500 text-xs">تغليف مزدوج للشاشات والمرايا والتحف القابلة للكسر.</p>
                        </div>
                    </div>

                    <!-- Photo 6 -->
                    <div class="group relative rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 bg-white border border-gray-200">
                        <img src="/assets/img/moving-team-jeddah-6.webp"
                            srcset="/assets/img/moving-team-jeddah-6-480.webp 480w, /assets/img/moving-team-jeddah-6.webp 800w"
                            sizes="(max-width: 768px) 100vw, 33vw"
                            alt="طاقم عمل شركة نجوم العرب أثناء إنجاز نقل الأثاث"
                            width="800" height="600" loading="lazy" decoding="async"
                            class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
                        <div class="p-4 bg-white text-right">
                            <h3 class="font-bold text-[#0a2540] text-base">فريق العمل أثناء النقل</h3>
                            <p class="text-gray-500 text-xs">عمالة مدربة على حمل وتنزيل الأثاث بانضباط وسرعة.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- O. Why Choose Us Section (6 Real Value Cards) -->
        <section id="whyus" class="py-20 bg-white border-b border-gray-200" aria-labelledby="whyus-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="text-center mb-16">
                    <span class="text-orange-500 font-bold text-lg tracking-wider">ثقة وأمان ومواعيد دقيقة</span>
                    <h2 id="whyus-heading" class="text-3xl md:text-5xl font-bold text-[#0a2540] mt-3 mb-4 leading-tight">
                        لماذا يفضل عملاؤنا نجوم العرب لنقل العفش؟
                    </h2>
                    <p class="text-gray-600 max-w-2xl mx-auto text-base sm:text-lg leading-relaxed">
                        نحرص على أن تكون عملية انتقالك منظمة ومريحة، عبر سيارات مجهزة وأطقم فنية خبيرة وأسعار مناسبة وواضحة.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 text-right">
                    <article class="bg-slate-50 rounded-2xl p-6 border border-gray-100 flex flex-col justify-between">
                        <div>
                            <div class="w-12 h-12 rounded-xl bg-orange-100 text-orange-600 flex items-center justify-center mb-4">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">الحرص على المواعيد</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">حضور فريق العمل وسيارات النقل في التوقيت المتفق عليه عند الحجز لإنجاز المهمة بسلاسة.</p>
                        </div>
                    </article>

                    <article class="bg-slate-50 rounded-2xl p-6 border border-gray-100 flex flex-col justify-between">
                        <div>
                            <div class="w-12 h-12 rounded-xl bg-orange-100 text-orange-600 flex items-center justify-center mb-4">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">عمالة وفنيون متخصصون</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">طواقم عمل خبيرة تضم نجارين لفك وتركيب الدواليب والمطابخ وعمالة مدربة على التحميل والتنزيل.</p>
                        </div>
                    </article>

                    <article class="bg-slate-50 rounded-2xl p-6 border border-gray-100 flex flex-col justify-between">
                        <div>
                            <div class="w-12 h-12 rounded-xl bg-orange-100 text-orange-600 flex items-center justify-center mb-4">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">عناية فائقة وتغليف متين</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">استخدام مواد تغليف أصلية تمنع الخدوش وتحافظ على نظافة وسلامة المفروشات والأجهزة.</p>
                        </div>
                    </article>

                    <article class="bg-slate-50 rounded-2xl p-6 border border-gray-100 flex flex-col justify-between">
                        <div>
                            <div class="w-12 h-12 rounded-xl bg-orange-100 text-orange-600 flex items-center justify-center mb-4">
                                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M20 8h-3V4H1v13h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">شاحنات مخصصة ومقفلة</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">أسطول سيارات دينا مجهز بصناديق مقفلة ومبطنة لحماية الأثاث من حرارة الجو والغبار والأمطار.</p>
                        </div>
                    </article>

                    <article class="bg-slate-50 rounded-2xl p-6 border border-gray-100 flex flex-col justify-between">
                        <div>
                            <div class="w-12 h-12 rounded-xl bg-orange-100 text-orange-600 flex items-center justify-center mb-4">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">أسعار واضحة وتنافسية</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">تسعير عادل ومحدد حسب حجم المنقولات والمسافة دون فرض أي رسوم غير متفق عليها مسبقاً.</p>
                        </div>
                    </article>

                    <article class="bg-slate-50 rounded-2xl p-6 border border-gray-100 flex flex-col justify-between">
                        <div>
                            <div class="w-12 h-12 rounded-xl bg-orange-100 text-orange-600 flex items-center justify-center mb-4">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">معاينة مجانية سريعة</h3>
                            <p class="text-gray-600 text-sm leading-relaxed">توفير خدمة المعاينة الميدانية أو التقدير الهاتفي الفوري لتحديد متطلبات النقل والتكلفة بدقة.</p>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <!-- P. FAQ Section (10 Questions - 100% Matching JSON-LD) -->
        <section id="faq" class="py-20 bg-slate-50 border-b border-gray-200" aria-labelledby="faq-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16 max-w-4xl">
                <div class="text-center mb-12">
                    <span class="text-orange-500 font-bold text-lg tracking-wider">إجابات واضحة لأسئلتك</span>
                    <h2 id="faq-heading" class="text-3xl md:text-5xl font-bold text-[#0a2540] mt-3 mb-4">
                        الأسئلة الشائعة حول نقل العفش بجدة
                    </h2>
                    <p class="text-gray-600 max-w-2xl mx-auto text-base sm:text-lg">
                        إجابات سريعة وشاملة عن أبرز استفسارات نقل الأثاث وفكه وتغليفه وتكلفته.
                    </p>
                </div>

                <div class="space-y-4" id="faqContainer">
                    <!-- Q1 -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-1" aria-expanded="false" aria-controls="faq-ans-1"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">ما الخدمات التي يشملها نقل العفش؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-1" role="region" aria-labelledby="faq-btn-1" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                تشمل خدماتنا الأساسية توفير العمالة وسيارات النقل، مع إمكانية إضافة خدمات مساندة مثل فك وتركيب الأثاث، وتغليف العفش، واستخدام ونش الرفع للأدوار المرتفعة حسب احتياجك.
                            </div>
                        </div>
                    </div>

                    <!-- Q2 -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-2" aria-expanded="false" aria-controls="faq-ans-2"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">كم سعر نقل العفش في جدة؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-2" role="region" aria-labelledby="faq-btn-2" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                تعتمد تكلفة نقل العفش في جدة على حجم المنقولات وعدد الغرف ومسافة النقل والأدوار. نوفر خيارات بأسعار مناسبة تبدأ من 350 ريال للاستوديو مع معاينة مجانية لتحديد التكلفة الدقيقة، ويمكنك مراجعة جدول التقديرات التوضيحي بالصفحة.
                            </div>
                        </div>
                    </div>

                    <!-- Q3 -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-3" aria-expanded="false" aria-controls="faq-ans-3"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">هل شركة نقل العفش في جدة توفر عمالة وفك وتركيب؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-3" role="region" aria-labelledby="faq-btn-3" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                نعم، نوفر طاقم عمل مدرباً يشمل نجارين متخصصين لفك وتركيب غرف النوم والمطابخ والمكاتب، مع تغليف كل قطعة وترقيم الملحقات لضمان إعادة تجميعها بإتقان وأمان تام.
                            </div>
                        </div>
                    </div>

                    <!-- Q4 -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-4" aria-expanded="false" aria-controls="faq-ans-4"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">ما أفضل وقت لحجز شركة نقل أثاث في جدة؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-4" role="region" aria-labelledby="faq-btn-4" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                كلما حجزت مبكراً كان توفر المواعيد وتنسيق سيارات النقل وفريق العمل أفضل، ويُفضل التواصل قبل الموعد بيوم أو يومين لتحديد الترتيبات المناسبة.
                            </div>
                        </div>
                    </div>

                    <!-- Q5 -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-5" aria-expanded="false" aria-controls="faq-ans-5"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">هل تنقلون العفش من جدة إلى مكة والمدينة والرياض وباقي المدن؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-5" role="region" aria-labelledby="faq-btn-5" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                نعم، نوفر رحلات شحن ونقل منتظمة بين المدن عبر شاحنات دينا مقفلة ومجهزة من جدة إلى الرياض، مكة المكرمة، المدينة المنورة، الطائف، والدمام مع تثبيت احترافي.
                            </div>
                        </div>
                    </div>

                    <!-- Q6 -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-6" aria-expanded="false" aria-controls="faq-ans-6"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">هل تخدمون جميع المناطق داخل جدة؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-6" role="region" aria-labelledby="faq-btn-6" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                نعم، نقدم خدمات النقل لمختلف أحياء ومناطق جدة بما فيها أحياء شمال ووسط وجنوب وشرق جدة لتسهيل عملية انتقالك داخل المدينة بكفاءة عالية.
                            </div>
                        </div>
                    </div>

                    <!-- Q7 -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-7" aria-expanded="false" aria-controls="faq-ans-7"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">هل تقومون بنقل أثاث المكاتب والفلل؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-7" role="region" aria-labelledby="faq-btn-7" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                بالتأكيد، نحن نتعامل مع مختلف أنواع العقارات بما في ذلك نقل الشقق، ونقل الفلل، بالإضافة إلى نقل وتجهيز مقرات المكاتب والشركات.
                            </div>
                        </div>
                    </div>

                    <!-- Q8 -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-8" aria-expanded="false" aria-controls="faq-ans-8"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">كم تستغرق عملية النقل؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-8" role="region" aria-labelledby="faq-btn-8" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                تعتمد المدة على حجم المنقولات والخدمات المطلوبة. عادةً ما تكتمل عمليات النقل الداخلية في نفس اليوم، ويتم الاتفاق على الوقت المتوقع عند المعاينة والحجز.
                            </div>
                        </div>
                    </div>

                    <!-- Q9 -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-9" aria-expanded="false" aria-controls="faq-ans-9"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">ما الذي يجب علي تجهيزه قبل وصول الفريق؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-9" role="region" aria-labelledby="faq-btn-9" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                يُفضل جمع المتعلقات الشخصية والمستندات الهامة، وفصل الأجهزة الكهربائية، وإخلاء الممرات لتسهيل عمل الفريق وضمان سرعة الإنجاز.
                            </div>
                        </div>
                    </div>

                    <!-- Q10 (New - Based on DATA) -->
                    <div class="faq-item bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                        <button type="button" id="faq-btn-10" aria-expanded="false" aria-controls="faq-ans-10"
                            class="w-full text-right faq-question flex justify-between items-center p-5 cursor-pointer hover:bg-gray-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-orange-400">
                            <h3 class="font-bold text-base sm:text-lg text-[#0a2540]">هل المعاينة الميدانية مجانية قبل الاتفاق؟</h3>
                            <svg class="w-5 h-5 text-orange-500 icon-arrow transition-transform duration-300 shrink-0 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        <div id="faq-ans-10" role="region" aria-labelledby="faq-btn-10" class="faq-answer">
                            <div class="p-5 pt-0 text-gray-600 text-sm leading-relaxed border-t border-gray-100">
                                نعم، نوفر خدمة المعاينة المجانية داخل أحياء جدة لتقدير حجم الأثاث وعدد الشاحنات المطلوبة والخدمات المساندة وتحديد التكلفة النهائية بدقة.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- R. Blog Section (6 Articles from Real Files) -->
        <section id="latest-blogs" class="py-20 bg-slate-50 border-b border-gray-200" aria-labelledby="blogs-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="text-center mb-16">
                    <span class="text-orange-500 font-bold text-lg tracking-wider">المدونة والنصائح</span>
                    <h2 id="blogs-heading" class="text-3xl md:text-4xl font-extrabold text-[#0a2540] mt-3 mb-4">
                        أحدث مقالات وإرشادات نقل العفش
                    </h2>
                    <p class="text-gray-600 max-w-2xl mx-auto text-base sm:text-lg">
                        دليل متجدد يساعدك في تنظيم وترتيب انتقالك السكني والتجاري بسلاسة.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 text-right">
                    <!-- Blog 1 -->
                    <article class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-100 flex flex-col justify-between">
                        <div class="p-6">
                            <span class="text-xs font-bold text-orange-500 bg-orange-500/10 px-3 py-1 rounded-full mb-4 inline-block">نصائح النقل</span>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-3 hover:text-orange-500 transition-colors">
                                <a href="./blogs/home-preparation-steps-before-moving/">خطوات تجهيز المنزل قبل نقل العفش</a>
                            </h3>
                            <p class="text-gray-600 text-sm leading-relaxed mb-4">
                                دليل شامل للتحضير لنقل الأثاث، التغليف، الفك، والاستعداد المنظم ليوم الانتقال الكبير في منزلك.
                            </p>
                        </div>
                        <div class="p-6 pt-0 border-t border-gray-50 flex items-center justify-between">
                            <a href="./blogs/home-preparation-steps-before-moving/" class="text-xs font-bold text-orange-500 hover:underline">قراءة المقال ←</a>
                        </div>
                    </article>

                    <!-- Blog 2 -->
                    <article class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-100 flex flex-col justify-between">
                        <div class="p-6">
                            <span class="text-xs font-bold text-orange-500 bg-orange-500/10 px-3 py-1 rounded-full mb-4 inline-block">تكلفة وأسعار</span>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-3 hover:text-orange-500 transition-colors">
                                <a href="./blogs/furniture-moving-prices-jeddah-2026/">دليل أسعار وتكلفة نقل العفش في جدة 2026</a>
                            </h3>
                            <p class="text-gray-600 text-sm leading-relaxed mb-4">
                                جدول استرشادي واقعي، تحليل العوامل المؤثرة، وكيفية مقارنة عروض الأسعار واختيار العرض الأنسب.
                            </p>
                        </div>
                        <div class="p-6 pt-0 border-t border-gray-50 flex items-center justify-between">
                            <a href="./blogs/furniture-moving-prices-jeddah-2026/" class="text-xs font-bold text-orange-500 hover:underline">قراءة المقال ←</a>
                        </div>
                    </article>

                    <!-- Blog 3 -->
                    <article class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-100 flex flex-col justify-between">
                        <div class="p-6">
                            <span class="text-xs font-bold text-orange-500 bg-orange-500/10 px-3 py-1 rounded-full mb-4 inline-block">حماية وتغليف</span>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-3 hover:text-orange-500 transition-colors">
                                <a href="./blogs/packing-fragile-electronics-glass-antiques/">تغليف الأجهزة الحساسة والتحف والزجاج</a>
                            </h3>
                            <p class="text-gray-600 text-sm leading-relaxed mb-4">
                                خطوات عملية لحماية الشاشات، المرايا، والتحف الثمينة من الكسر والخدوش بأحدث خامات التغليف.
                            </p>
                        </div>
                        <div class="p-6 pt-0 border-t border-gray-50 flex items-center justify-between">
                            <a href="./blogs/packing-fragile-electronics-glass-antiques/" class="text-xs font-bold text-orange-500 hover:underline">قراءة المقال ←</a>
                        </div>
                    </article>

                    <!-- Blog 4 -->
                    <article class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-100 flex flex-col justify-between">
                        <div class="p-6">
                            <span class="text-xs font-bold text-orange-500 bg-orange-500/10 px-3 py-1 rounded-full mb-4 inline-block">حماية الأثاث</span>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-3 hover:text-orange-500 transition-colors">
                                <a href="./blogs/protecting-furniture-jeddah-heat-humidity/">حماية الأثاث من حرارة ورطوبة جدة</a>
                            </h3>
                            <p class="text-gray-600 text-sm leading-relaxed mb-4">
                                نصائح لحماية الأثاث الخشبي والمفروشات والأجهزة من الرطوبة والحرارة أثناء النقل والتخزين بجدة.
                            </p>
                        </div>
                        <div class="p-6 pt-0 border-t border-gray-50 flex items-center justify-between">
                            <a href="./blogs/protecting-furniture-jeddah-heat-humidity/" class="text-xs font-bold text-orange-500 hover:underline">قراءة المقال ←</a>
                        </div>
                    </article>

                    <!-- Blog 5 -->
                    <article class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-100 flex flex-col justify-between">
                        <div class="p-6">
                            <span class="text-xs font-bold text-orange-500 bg-orange-500/10 px-3 py-1 rounded-full mb-4 inline-block">قائمة فحص</span>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-3 hover:text-orange-500 transition-colors">
                                <a href="./blogs/new-home-moving-checklist-jeddah/">قائمة المراجعة الشاملة للانتقال لبيت جديد</a>
                            </h3>
                            <p class="text-gray-600 text-sm leading-relaxed mb-4">
                                قائمة تفاعلية مجدولة زمنياً لمراحل ما قبل النقل، يوم النقل، وما بعد الوصول للمنزل الجديد بجدة.
                            </p>
                        </div>
                        <div class="p-6 pt-0 border-t border-gray-50 flex items-center justify-between">
                            <a href="./blogs/new-home-moving-checklist-jeddah/" class="text-xs font-bold text-orange-500 hover:underline">قراءة المقال ←</a>
                        </div>
                    </article>

                    <!-- Blog 6 -->
                    <article class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-100 flex flex-col justify-between">
                        <div class="p-6">
                            <span class="text-xs font-bold text-orange-500 bg-orange-500/10 px-3 py-1 rounded-full mb-4 inline-block">دليل الاختيار</span>
                            <h3 class="text-xl font-bold text-[#0a2540] mb-3 hover:text-orange-500 transition-colors">
                                <a href="./blogs/how-to-choose-best-moving-company-in-jeddah/">كيف تختار أفضل شركة نقل عفش في جدة؟</a>
                            </h3>
                            <p class="text-gray-600 text-sm leading-relaxed mb-4">
                                معايير عملية وأسئلة أساسية تساعدك في تقييم خدمات نقل العفش واختيار الشركة المناسبة بثقة.
                            </p>
                        </div>
                        <div class="p-6 pt-0 border-t border-gray-50 flex items-center justify-between">
                            <a href="./blogs/how-to-choose-best-moving-company-in-jeddah/" class="text-xs font-bold text-orange-500 hover:underline">قراءة المقال ←</a>
                        </div>
                    </article>
                </div>

                <div class="text-center mt-12">
                    <a href="./blogs/"
                        class="inline-block bg-[#0a2540] hover:bg-[#081d33] text-white text-sm font-bold px-8 py-3 rounded-full transition-colors">
                        عرض جميع مقالات المدونة ←
                    </a>
                </div>
            </div>
        </section>

        <!-- S. Contact & NAP Section -->
        <section id="contact" class="py-20 bg-white border-b border-gray-200" aria-labelledby="contact-heading">
            <div class="container mx-auto px-4 md:px-8 lg:px-16">
                <div class="flex flex-col lg:flex-row gap-12">

                    <!-- NAP Info Column -->
                    <div class="w-full lg:w-5/12 text-right">
                        <span class="text-orange-500 font-bold text-sm tracking-wider block mb-2">تواصل مباشر وسريع</span>
                        <h2 id="contact-heading" class="text-3xl md:text-4xl font-extrabold text-[#0a2540] mb-6">
                            اتصل بنا أو احجز معاينتك المجانية
                        </h2>
                        <p class="text-gray-600 text-base leading-relaxed mb-8">
                            فريق خدمة العملاء متواجد للإجابة على استفساراتكم وحجز مواعيد المعاينة ونقل العفش في كافة أحياء جدة.
                        </p>

                        <!-- Consistent NAP Block -->
                        <div class="space-y-4 mb-8">
                            <div class="flex items-start gap-3">
                                <div class="w-10 h-10 rounded-xl bg-orange-50 text-orange-500 flex items-center justify-center shrink-0">
                                    <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
                                </div>
                                <div>
                                    <h3 class="font-bold text-[#0a2540] text-sm">العنوان الميداني:</h3>
                                    <p class="text-gray-600 text-xs sm:text-sm">جدة – حي مشرفة – شارع الصحافة – خلف مرور الصحافة</p>
                                </div>
                            </div>

                            <div class="flex items-start gap-3">
                                <div class="w-10 h-10 rounded-xl bg-orange-50 text-orange-500 flex items-center justify-center shrink-0">
                                    <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1.003 1.003 0 011.02-.24c1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                                </div>
                                <div>
                                    <h3 class="font-bold text-[#0a2540] text-sm">الهاتف المباشر:</h3>
                                    <a href="tel:+966500504024" class="text-gray-600 text-xs sm:text-sm hover:text-orange-500 font-bold">0500504024</a>
                                </div>
                            </div>

                            <div class="flex items-start gap-3">
                                <div class="w-10 h-10 rounded-xl bg-orange-50 text-orange-500 flex items-center justify-center shrink-0">
                                    <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                </div>
                                <div>
                                    <h3 class="font-bold text-[#0a2540] text-sm">ساعات العمل:</h3>
                                    <p class="text-gray-600 text-xs sm:text-sm">السبت – الخميس: 9:00 ص – 9:00 م (الجمعة مغلق)</p>
                                </div>
                            </div>
                        </div>

                        <!-- Social Media Links -->
                        <div class="flex items-center gap-3 pt-2">
                            <span class="text-xs font-bold text-gray-700">تابعنا على:</span>
                            <a href="https://www.facebook.com/share/1CxAfotMzu/" target="_blank" rel="noopener noreferrer"
                                class="w-9 h-9 rounded-full bg-slate-100 hover:bg-orange-500 hover:text-white text-[#0a2540] flex items-center justify-center transition-colors shadow-sm"
                                aria-label="صفحة شركة نجوم العرب لنقل الأثاث على فيسبوك">
                                <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                            </a>
                            <a href="https://www.instagram.com/nngoom33" target="_blank" rel="noopener noreferrer"
                                class="w-9 h-9 rounded-full bg-slate-100 hover:bg-orange-500 hover:text-white text-[#0a2540] flex items-center justify-center transition-colors shadow-sm"
                                aria-label="حساب شركة نجوم العرب لنقل الأثاث على إنستغرام">
                                <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                            </a>
                        </div>
                    </div>

                    <!-- Contact Form Column -->
                    <div class="w-full lg:w-7/12">
                        <div class="bg-slate-50 p-8 rounded-3xl border border-gray-200 shadow-sm text-right">
                            <h3 class="text-xl font-bold text-[#0a2540] mb-2">اطلب عرض سعر فوري</h3>
                            <p class="text-gray-600 text-xs sm:text-sm mb-6">
                                املأ البيانات أدناه وسنتواصل معك فوراً لتحديد تفاصيل النقل أو ترتيب المعاينة المجانية.
                            </p>

                            <form id="contactForm" class="space-y-4">
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                    <div>
                                        <label for="c_name" class="block text-xs font-bold text-gray-700 mb-1">الاسم الكريم:</label>
                                        <input type="text" id="c_name" required placeholder="اسمك"
                                            class="w-full px-4 py-3 rounded-xl border border-gray-300 text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white">
                                    </div>
                                    <div>
                                        <label for="c_phone" class="block text-xs font-bold text-gray-700 mb-1">رقم الجوال:</label>
                                        <input type="tel" id="c_phone" required placeholder="05XXXXXXXX" pattern="^(05|5|\+9665)[0-9]{8}$"
                                            class="w-full px-4 py-3 rounded-xl border border-gray-300 text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white text-left" dir="ltr">
                                    </div>
                                </div>

                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                    <div>
                                        <label for="c_service" class="block text-xs font-bold text-gray-700 mb-1">نوع الخدمة المطلوبة:</label>
                                        <select id="c_service"
                                            class="w-full px-4 py-3 rounded-xl border border-gray-300 text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white">
                                            <option value="نقل عفش شقة">نقل عفش شقة</option>
                                            <option value="نقل عفش فيلا">نقل عفش فيلا</option>
                                            <option value="نقل أثاث مكتب أو شركة">نقل أثاث مكتب أو شركة</option>
                                            <option value="فك وتركيب أثاث فقط">فك وتركيب أثاث فقط</option>
                                            <option value="تغليف أثاث">تغليف أثاث</option>
                                            <option value="نقل بين المدن">نقل بين المدن</option>
                                            <option value="معاينة مجانية">طلب معاينة مجانية</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label for="c_area" class="block text-xs font-bold text-gray-700 mb-1">الحي أو المنطقة:</label>
                                        <input type="text" id="c_area" placeholder="مثال: حي الروضة، الحمدانية..."
                                            class="w-full px-4 py-3 rounded-xl border border-gray-300 text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white">
                                    </div>
                                </div>

                                <div>
                                    <label for="c_notes" class="block text-xs font-bold text-gray-700 mb-1">تفاصيل إضافية (اختياري):</label>
                                    <textarea id="c_notes" rows="3" placeholder="عدد الغرف، الأدوار، توفر مصعد..."
                                        class="w-full px-4 py-3 rounded-xl border border-gray-300 text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white"></textarea>
                                </div>

                                <button type="submit"
                                    class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3.5 rounded-xl transition-colors shadow-md text-base flex items-center justify-center gap-2">
                                    <span>إرسال الطلب عبر واتساب</span>
                                    <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.205 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                                </button>
                            </form>
                        </div>
                    </div>

                </div>
            </div>
        </section>
    </main>

    <!-- T. Inline Footer (Cleaned, no h2/h3 pollution) -->
    <footer id="global-site-footer" class="text-white pt-16 pb-8 bg-[#0a2540] border-t-4 border-orange-500">
        <div class="container mx-auto px-4 md:px-8 lg:px-12">

            <!-- Top Value Bar (<p> tags instead of h2/h3) -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pb-10 mb-10 border-b border-white/10">
                <div class="flex items-center gap-3.5 p-4 rounded-2xl bg-white/5 border border-white/10">
                    <div class="w-10 h-10 rounded-xl flex items-center justify-center text-orange-400 bg-orange-400/10">
                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M20 8h-3V4H1v13h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4z"/></svg>
                    </div>
                    <div>
                        <p class="text-sm font-bold text-white mb-0.5">أسطول دينا مجهز</p>
                        <p class="text-xs text-gray-300">شاحنات مقفلة ومخصصة للأثاث</p>
                    </div>
                </div>
                <div class="flex items-center gap-3.5 p-4 rounded-2xl bg-white/5 border border-white/10">
                    <div class="w-10 h-10 rounded-xl flex items-center justify-center text-orange-400 bg-orange-400/10">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                    </div>
                    <div>
                        <p class="text-sm font-bold text-white mb-0.5">عناية وأمان تام</p>
                        <p class="text-xs text-gray-300">حماية فائقة من الخدوش والكسر</p>
                    </div>
                </div>
                <div class="flex items-center gap-3.5 p-4 rounded-2xl bg-white/5 border border-white/10">
                    <div class="w-10 h-10 rounded-xl flex items-center justify-center text-orange-400 bg-orange-400/10">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M11 4a2 2 0 114 0v1a2 2 0 01-2 2 2 2 0 01-2-2V4zm2 6a2 2 0 012 2v7a2 2 0 01-2 2 2 2 0 01-2-2v-7a2 2 0 012-2z"/></svg>
                    </div>
                    <div>
                        <p class="text-sm font-bold text-white mb-0.5">نجارون متخصصون</p>
                        <p class="text-xs text-gray-300">فك وتركيب غرف ومطابخ باحتراف</p>
                    </div>
                </div>
                <div class="flex items-center gap-3.5 p-4 rounded-2xl bg-white/5 border border-white/10">
                    <div class="w-10 h-10 rounded-xl flex items-center justify-center text-orange-400 bg-orange-400/10">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                    <div>
                        <p class="text-sm font-bold text-white mb-0.5">أسعار مناسبة</p>
                        <p class="text-xs text-gray-300">معاينة مجانية وعروض واضحة</p>
                    </div>
                </div>
            </div>

            <!-- Main Footer Links Grid (<p class="font-bold"> headers) -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8 pb-12 border-b border-white/10 text-right">

                <!-- Col 1: Brand Info -->
                <div class="lg:col-span-1">
                    <div class="flex items-center gap-3 mb-4">
                        <img src="/assets/img/logo-128.webp" alt="شعار نجوم العرب" width="48" height="48"
                            class="w-12 h-12 rounded-full object-contain bg-white/5 border border-white/10 p-1">
                        <div>
                            <span class="text-base font-bold text-white">نجوم العرب</span>
                            <span class="block text-xs text-orange-400">نقل أثاث بجدة</span>
                        </div>
                    </div>
                    <p class="text-xs text-gray-300 leading-relaxed mb-4">
                        شركة متخصصة في نقل وتغليف وفك وتركيب الأثاث والعفش السكني والتجاري داخل وخارج جدة.
                    </p>
                    <div class="flex items-center gap-2">
                        <a href="https://www.facebook.com/share/1CxAfotMzu/" target="_blank" rel="noopener noreferrer"
                            class="w-8 h-8 rounded-full bg-white/10 hover:bg-orange-500 text-white flex items-center justify-center transition-colors"
                            aria-label="فيسبوك شركة نجوم العرب">
                            <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                        </a>
                        <a href="https://www.instagram.com/nngoom33" target="_blank" rel="noopener noreferrer"
                            class="w-8 h-8 rounded-full bg-white/10 hover:bg-orange-500 text-white flex items-center justify-center transition-colors"
                            aria-label="إنستغرام شركة نجوم العرب">
                            <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                        </a>
                    </div>
                </div>

                <!-- Col 2: Core Services -->
                <div>
                    <p class="font-bold text-sm text-white mb-3">خدمات النقل الأساسية</p>
                    <ul class="text-xs text-gray-300 space-y-2">
                        <li><a href="./services/" class="hover:text-orange-400">جميع خدمات نقل الأثاث</a></li>
                        <li><a href="./furniture-disassembly-and-reassembly-in-jeddah/" class="hover:text-orange-400">فك وتركيب العفش</a></li>
                        <li><a href="./furniture-packaging-in-jeddah/" class="hover:text-orange-400">تغليف العفش بالبابلز</a></li>
                        <li><a href="./furniture-transport-trucks-in-jeddah/" class="hover:text-orange-400">سيارات دينا لنقل العفش</a></li>
                        <li><a href="./furniture-lifting-crane-in-jeddah/" class="hover:text-orange-400">ونش رفع عفش بجدة</a></li>
                        <li><a href="./furniture-storage-in-jeddah/" class="hover:text-orange-400">مستودعات تخزين الأثاث</a></li>
                    </ul>
                </div>

                <!-- Col 3: Additional Services (The 6 Extra Services) -->
                <div>
                    <p class="font-bold text-sm text-white mb-3">خدمات تخصصية إضافية</p>
                    <ul class="text-xs text-gray-300 space-y-2">
                        <li><a href="./ikea-furniture-moving-jeddah/" class="hover:text-orange-400">فك ونقل أثاث ايكيا</a></li>
                        <li><a href="./kitchen-moving-jeddah/" class="hover:text-orange-400">نقل المطابخ والرخام</a></li>
                        <li><a href="./ac-disassembly-and-moving-jeddah/" class="hover:text-orange-400">فك ونقل مكيفات سبليت</a></li>
                        <li><a href="./old-furniture-removal-jeddah/" class="hover:text-orange-400">إزالة الأثاث القديم والرجيع</a></li>
                        <li><a href="./small-moving-truck-jeddah/" class="hover:text-orange-400">ونيت ودينا صغيرة للمشاوير</a></li>
                        <li><a href="./filipino-moving-labour-jeddah/" class="hover:text-orange-400">عمالة فلبينية لنقل العفش</a></li>
                    </ul>
                </div>

                <!-- Col 4: Property Types & Pricing -->
                <div>
                    <p class="font-bold text-sm text-white mb-3">العقارات والأسعار</p>
                    <ul class="text-xs text-gray-300 space-y-2">
                        <li><a href="./apartment-furniture-moving-jeddah/" class="hover:text-orange-400">نقل عفش الشقق</a></li>
                        <li><a href="./villa-moving-jeddah/" class="hover:text-orange-400">نقل عفش الفلل والقصور</a></li>
                        <li><a href="./office-furniture-moving-jeddah/" class="hover:text-orange-400">نقل مكاتب وشركات</a></li>
                        <li><a href="./furniture-moving-prices-jeddah/" class="hover:text-orange-400">أسعار نقل العفش بجدة</a></li>
                        <li><a href="./affordable-furniture-moving-jeddah/" class="hover:text-orange-400">نقل أثاث اقتصادي</a></li>
                        <li><a href="./carpenter-furniture-disassembly-assembly-jeddah/" class="hover:text-orange-400">نجار فك وتركيب بجدة</a></li>
                    </ul>
                </div>

                <!-- Col 5: Intercity & Areas -->
                <div>
                    <p class="font-bold text-sm text-white mb-3">النقل بين المدن والأحياء</p>
                    <ul class="text-xs text-gray-300 space-y-2">
                        <li><a href="./areas/" class="hover:text-orange-400 font-bold text-orange-400">تغطية أحياء جدة العشرة</a></li>
                        <li><a href="./intercity-moving/" class="hover:text-orange-400">نقل بين المدن من جدة</a></li>
                        <li><a href="./intercity-moving/jeddah-to-riyadh/" class="hover:text-orange-400">نقل عفش من جدة للرياض</a></li>
                        <li><a href="./intercity-moving/jeddah-to-makkah/" class="hover:text-orange-400">نقل عفش من جدة لمكة</a></li>
                        <li><a href="./intercity-moving/jeddah-to-madinah/" class="hover:text-orange-400">نقل عفش من جدة للمدينة</a></li>
                        <li><a href="./intercity-moving/jeddah-to-taif/" class="hover:text-orange-400">نقل عفش من جدة للطائف</a></li>
                        <li><a href="./intercity-moving/jeddah-to-dammam/" class="hover:text-orange-400">نقل عفش من جدة للدمام</a></li>
                    </ul>
                </div>

            </div>

            <!-- Copyright & Legal -->
            <div class="pt-6 flex flex-col sm:flex-row justify-between items-center gap-4 text-xs text-gray-400">
                <p>© <span id="currentYear">2026</span> شركة نجوم العرب لنقل الأثاث بجدة – جميع الحقوق محفوظة</p>
                <div class="flex gap-4">
                    <a href="./privacy-policy.html" class="hover:text-orange-400">سياسة الخصوصية</a>
                    <span>•</span>
                    <a href="./terms.html" class="hover:text-orange-400">الشروط والأحكام</a>
                    <span>•</span>
                    <a href="./sitemap.xml" class="hover:text-orange-400">خريطة الموقع</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- U. Floating Contact Buttons -->
    <div class="fixed bottom-6 right-5 z-[9999] flex flex-col gap-3">
        <a href="https://wa.me/966500504024" target="_blank" rel="noopener noreferrer"
            aria-label="تواصل عبر واتساب مع نجوم العرب لنقل العفش بجدة"
            class="w-14 h-14 bg-green-500 hover:bg-green-600 rounded-full shadow-2xl flex items-center justify-center transition-transform hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white">
            <svg class="w-7 h-7 fill-white" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.205 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
        </a>
        <a href="tel:+966500504024" aria-label="الاتصال بشركة نجوم العرب لنقل العفش بجدة"
            class="w-14 h-14 bg-orange-500 hover:bg-orange-600 rounded-full shadow-2xl flex items-center justify-center transition-transform hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white">
            <svg class="w-6 h-6 fill-white" viewBox="0 0 24 24"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1.003 1.003 0 011.02-.24c1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
        </a>
    </div>

    <!-- Client-side Scripts -->
    <script>
        // Update Copyright Year
        var yr = document.getElementById('currentYear');
        if (yr) yr.textContent = new Date().getFullYear();

        // Mobile Menu Toggle
        var menuBtn = document.getElementById('mobileMenuBtn');
        var mobileMenu = document.getElementById('mobileMenu');
        if (menuBtn && mobileMenu) {{
            menuBtn.addEventListener('click', function () {{
                var isExpanded = menuBtn.getAttribute('aria-expanded') === 'true';
                menuBtn.setAttribute('aria-expanded', !isExpanded);
                mobileMenu.classList.toggle('hidden');
            }});
        }}

        // Accessible FAQ Accordion
        var faqBtns = document.querySelectorAll('.faq-question');
        faqBtns.forEach(function (btn) {{
            btn.addEventListener('click', function () {{
                var isExpanded = btn.getAttribute('aria-expanded') === 'true';
                var targetId = btn.getAttribute('aria-controls');
                var answerEl = document.getElementById(targetId);
                var arrowIcon = btn.querySelector('.icon-arrow');

                // Close all others
                faqBtns.forEach(function (otherBtn) {{
                    if (otherBtn !== btn) {{
                        otherBtn.setAttribute('aria-expanded', 'false');
                        var otherTarget = document.getElementById(otherBtn.getAttribute('aria-controls'));
                        if (otherTarget) otherTarget.classList.remove('active');
                        var otherArrow = otherBtn.querySelector('.icon-arrow');
                        if (otherArrow) otherArrow.classList.remove('rotate-180');
                    }}
                }});

                // Toggle current
                btn.setAttribute('aria-expanded', !isExpanded);
                if (answerEl) answerEl.classList.toggle('active', !isExpanded);
                if (arrowIcon) arrowIcon.classList.toggle('rotate-180', !isExpanded);
            }});
        }});

        // Contact Form Submission via WhatsApp
        var contactForm = document.getElementById('contactForm');
        if (contactForm) {{
            contactForm.addEventListener('submit', function (e) {{
                e.preventDefault();
                var name = (document.getElementById('c_name').value || '').trim();
                var phone = (document.getElementById('c_phone').value || '').trim();
                var service = document.getElementById('c_service').value;
                var area = (document.getElementById('c_area').value || '').trim();
                var notes = (document.getElementById('c_notes').value || '').trim();

                var msg = "مرحباً نجوم العرب، أرغب في حجز خدمة نقل عفش بجدة:\\n" +
                    "- الاسم: " + name + "\\n" +
                    "- الجوال: " + phone + "\\n" +
                    "- نوع الخدمة: " + service + "\\n" +
                    (area ? "- الحي: " + area + "\\n" : "") +
                    (notes ? "- ملاحظات إضافية: " + notes + "\\n" : "");

                var waUrl = "https://wa.me/966500504024?text=" + encodeURIComponent(msg);
                window.open(waUrl, '_blank');
            }});
        }}
    </script>
</body>

</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated clean and complete index.html successfully.')

