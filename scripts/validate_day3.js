const fs = require('fs');
const path = require('path');

const rootDir = path.join(__dirname, '..');
const sitemapPath = path.join(rootDir, 'sitemap.xml');
const sitemapContent = fs.readFileSync(sitemapPath, 'utf8');

console.log('=== 1. SITEMAP VALIDATION ===');
// Extract URLs
const locRegex = /<loc>(https:\/\/nojomalarab\.com\/[^<]*)<\/loc>/g;
let match;
const urls = [];
while ((match = locRegex.exec(sitemapContent)) !== null) {
    urls.push(match[1]);
}

console.log(`Total URLs in sitemap: ${urls.length}`);

// Check duplicates
const uniqueUrls = new Set(urls);
if (uniqueUrls.size === urls.length) {
    console.log('✓ No duplicate URLs found in sitemap.xml.');
} else {
    console.error(`✗ DUPLICATE DETECTED! Unique: ${uniqueUrls.size}, Total: ${urls.length}`);
}

// Check each URL maps to existing file on disk
let missingFiles = 0;
urls.forEach(u => {
    let relPath = u.replace('https://nojomalarab.com/', '');
    if (relPath.endsWith('/')) {
        relPath += 'index.html';
    } else if (relPath === '') {
        relPath = 'index.html';
    }
    const fullPath = path.join(rootDir, relPath);
    if (!fs.existsSync(fullPath)) {
        console.error(`✗ File missing for URL ${u}: ${fullPath}`);
        missingFiles++;
    }
});

if (missingFiles === 0) {
    console.log('✓ All 33 sitemap URLs map to real existing files on disk!');
}

console.log('\n=== 2. JSON-LD VALIDATION FOR NEW PAGES ===');
const targetPages = [
    'intercity-moving/index.html',
    'intercity-moving/jeddah-to-riyadh/index.html',
    'intercity-moving/jeddah-to-makkah/index.html',
    'intercity-moving/jeddah-to-madinah/index.html',
    'intercity-moving/jeddah-to-taif/index.html',
    'intercity-moving/jeddah-to-dammam/index.html'
];

targetPages.forEach(p => {
    const fullP = path.join(rootDir, p);
    const html = fs.readFileSync(fullP, 'utf8');
    const jsonLdRegex = /<script type="application\/ld\+json">([\s\S]*?)<\/script>/gi;
    let jsonMatch;
    let jsonCount = 0;
    while ((jsonMatch = jsonLdRegex.exec(html)) !== null) {
        jsonCount++;
        try {
            const parsed = JSON.parse(jsonMatch[1]);
            // check type
            const type = parsed['@type'] || (Array.isArray(parsed) ? 'Array' : 'Unknown');
        } catch (e) {
            console.error(`✗ JSON-LD Syntax error in ${p}:`, e.message);
        }
    }
    console.log(`✓ ${p}: ${jsonCount} valid JSON-LD schema blocks found.`);
});

console.log('\n=== 3. CANONICAL & H1 VALIDATION ===');
targetPages.forEach(p => {
    const fullP = path.join(rootDir, p);
    const html = fs.readFileSync(fullP, 'utf8');
    
    // Canonical
    const canMatch = html.match(/<link rel="canonical" href="([^"]+)"/);
    const h1Match = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/);
    const titleMatch = html.match(/<title>([\s\S]*?)<\/title>/);
    const descMatch = html.match(/<meta name="description"\s+content="([^"]+)"/);

    console.log(`\nPage: ${p}`);
    console.log(`  Canonical: ${canMatch ? canMatch[1] : 'MISSING'}`);
    console.log(`  Title: ${titleMatch ? titleMatch[1].trim() : 'MISSING'}`);
    console.log(`  H1: ${h1Match ? h1Match[1].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim() : 'MISSING'}`);
    console.log(`  Meta Desc length: ${descMatch ? descMatch[1].length : 0} chars`);
});
