const fs = require('fs');
const path = require('path');

console.log('=== STARTING AUTOMATED VALIDATION SUITE ===\n');

let passCount = 0;
let failCount = 0;

function assert(condition, message) {
    if (condition) {
        console.log(`[PASS] ${message}`);
        passCount++;
    } else {
        console.error(`[FAIL] ${message}`);
        failCount++;
    }
}

// 1. Validate sitemap.xml
console.log('--- 1. Testing sitemap.xml ---');
const sitemapContent = fs.readFileSync('sitemap.xml', 'utf8');
assert(sitemapContent.startsWith('<?xml'), 'sitemap starts with XML declaration');
assert(sitemapContent.includes('</urlset>'), 'sitemap ends with </urlset>');

const locMatches = [...sitemapContent.matchAll(/<loc>(.*?)<\/loc>/g)].map(m => m[1]);
assert(locMatches.length === 35, `sitemap has exactly 35 URLs (got ${locMatches.length})`);

const expectedNewUrls = [
    'https://nojomalarab.com/blogs/furniture-moving-prices-jeddah-2026/',
    'https://nojomalarab.com/blogs/packing-fragile-electronics-glass-antiques/',
    'https://nojomalarab.com/blogs/protecting-furniture-jeddah-heat-humidity/',
    'https://nojomalarab.com/blogs/new-home-moving-checklist-jeddah/'
];

expectedNewUrls.forEach(url => {
    assert(locMatches.includes(url), `sitemap includes new URL: ${url}`);
});

// Check lastmod of blogs/
const blogsLastmodMatch = sitemapContent.match(/<loc>https:\/\/nojomalarab\.com\/blogs\/<\/loc>\s*<lastmod>(.*?)<\/lastmod>/);
assert(blogsLastmodMatch && blogsLastmodMatch[1].startsWith('2026-10-18'), 'blogs/ index has lastmod 2026-10-18');

// 2. Validate Blog Articles
console.log('\n--- 2. Testing 4 New Articles Files & Content ---');
const articlesToCheck = [
    {
        path: 'blogs/furniture-moving-prices-jeddah-2026/index.html',
        canonical: 'https://nojomalarab.com/blogs/furniture-moving-prices-jeddah-2026/',
        expectedH1: 'دليل أسعار وتكلفة نقل العفش في جدة 2026',
        primaryKeyword: 'أسعار نقل العفش بجدة',
        image: 'assets/img/furniture-moving-in-jeddah.webp'
    },
    {
        path: 'blogs/packing-fragile-electronics-glass-antiques/index.html',
        canonical: 'https://nojomalarab.com/blogs/packing-fragile-electronics-glass-antiques/',
        expectedH1: 'الدليل الشامل لتغليف الأجهزة الحساسة والتحف والزجاج أثناء النقل دون تعريضها للكسر',
        primaryKeyword: 'تغليف الأجهزة الحساسة والتحف والزجاج',
        image: 'assets/img/furniture-packaging-in-jeddah.webp'
    },
    {
        path: 'blogs/protecting-furniture-jeddah-heat-humidity/index.html',
        canonical: 'https://nojomalarab.com/blogs/protecting-furniture-jeddah-heat-humidity/',
        expectedH1: 'كيف تحمي أثاثك أثناء النقل في جدة؟ نصائح عملية للتعامل مع الحرارة والرطوبة',
        primaryKeyword: 'حماية الأثاث أثناء النقل في جدة',
        image: 'assets/img/furniture-storage-in-jeddah.webp'
    },
    {
        path: 'blogs/new-home-moving-checklist-jeddah/index.html',
        canonical: 'https://nojomalarab.com/blogs/new-home-moving-checklist-jeddah/',
        expectedH1: 'قائمة المراجعة الشاملة للانتقال إلى بيت جديد في جدة: Checklist قبل وأثناء وبعد النقل',
        primaryKeyword: 'قائمة تجهيز الانتقال إلى بيت جديد في جدة',
        image: 'assets/img/furniture-transport-trucks-in-jeddah.webp'
    }
];

articlesToCheck.forEach(art => {
    console.log(`\nTesting article: ${art.path}`);
    assert(fs.existsSync(art.path), `File exists: ${art.path}`);
    const html = fs.readFileSync(art.path, 'utf8');

    // Canonical
    assert(html.includes(`rel="canonical" href="${art.canonical}"`), `Canonical matches ${art.canonical}`);

    // Title tag
    const titleMatch = html.match(/<title>(.*?)<\/title>/);
    assert(titleMatch && titleMatch[1].length > 20, `Valid Title Tag: ${titleMatch ? titleMatch[1] : 'NONE'}`);

    // Meta Description
    const descMatch = html.match(/<meta\s+name="description"\s+content="(.*?)"/);
    assert(descMatch && descMatch[1].length > 50, `Valid Meta Description (${descMatch ? descMatch[1].length : 0} chars)`);

    // Single H1
    const h1Matches = [...html.matchAll(/<h1[^>]*>(.*?)<\/h1>/gs)];
    assert(h1Matches.length === 1, `Exactly one H1 found (count: ${h1Matches.length})`);
    assert(h1Matches[0][1].includes(art.expectedH1) || art.expectedH1.includes(h1Matches[0][1].trim()), `H1 matches expectation`);

    // Primary Keyword present
    assert(html.includes(art.primaryKeyword), `Primary keyword "${art.primaryKeyword}" is present in content`);

    // Check image file exists on disk
    assert(fs.existsSync(art.image), `Featured image exists on disk: ${art.image}`);

    // JSON-LD Schemas syntax check
    const jsonLdMatches = [...html.matchAll(/<script type="application\/ld\+json">(.*?)<\/script>/gs)];
    assert(jsonLdMatches.length >= 2, `Found ${jsonLdMatches.length} JSON-LD schemas`);
    jsonLdMatches.forEach((script, idx) => {
        try {
            const parsed = JSON.parse(script[1].trim());
            assert(parsed['@context'] === 'https://schema.org', `Schema #${idx+1} valid @context`);
            assert(parsed['@type'], `Schema #${idx+1} has @type: ${parsed['@type']}`);
        } catch (e) {
            assert(false, `Schema #${idx+1} failed JSON.parse: ${e.message}`);
        }
    });

    // Verify footer script
    assert(html.includes('id="site-footer"'), 'Contains #site-footer element');
    assert(html.includes('src="/assets/js/footer.js"'), 'Contains footer.js loader');
});

// 3. Validate blogs/index.html
console.log('\n--- 3. Testing blogs/index.html ---');
const blogIndexHtml = fs.readFileSync('blogs/index.html', 'utf8');
assert(blogIndexHtml.includes('id="articlesGrid"'), 'Contains #articlesGrid');

// Check that all 4 new slugs are in the articles array
expectedNewUrls.forEach(url => {
    const slug = url.split('/').filter(Boolean).pop();
    assert(blogIndexHtml.includes(`./${slug}/`), `blogs/index.html references ./${slug}/`);
});

// Check that all 7 article images exist on disk
const articleImagePaths = [
    'assets/img/furniture-moving-in-jeddah.webp',
    'assets/img/furniture-packaging-in-jeddah.webp',
    'assets/img/furniture-storage-in-jeddah.webp',
    'assets/img/furniture-transport-trucks-in-jeddah.webp',
    "assets/img/furniture-moving-across-jeddah's-neighborhoods-and-districts.webp",
    'assets/img/about.webp',
    'assets/img/furniture-disassembly-and-reassembly-in-jeddah.webp'
];

articleImagePaths.forEach(imgPath => {
    assert(fs.existsSync(imgPath), `Article card image exists on disk: ${imgPath}`);
});

console.log(`\n=== SUITE FINISHED: ${passCount} PASSED, ${failCount} FAILED ===`);
if (failCount > 0) process.exit(1);
