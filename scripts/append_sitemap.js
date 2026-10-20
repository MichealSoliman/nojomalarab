const fs = require('fs');
const path = require('path');

const sitemapPath = path.join(__dirname, '..', 'sitemap.xml');
let content = fs.readFileSync(sitemapPath, 'utf8');

// 1. Update lastmod for modified pages only
content = content.replace(
    /(<loc>https:\/\/nojomalarab\.com\/<\/loc>\s*<lastmod>)[^<]+(<\/lastmod>)/,
    '$12026-10-20T12:00:00+00:00$2'
);

content = content.replace(
    /(<loc>https:\/\/nojomalarab\.com\/intercity-furniture-moving-from-jeddah\/<\/loc>\s*<lastmod>)[^<]+(<\/lastmod>)/,
    '$12026-10-20T12:00:00+00:00$2'
);

// 2. The 6 new URLs to append before </urlset>
const newUrls = [
    {
        loc: 'https://nojomalarab.com/intercity-moving/',
        lastmod: '2026-10-20T12:00:00+00:00',
        priority: '0.85'
    },
    {
        loc: 'https://nojomalarab.com/intercity-moving/jeddah-to-riyadh/',
        lastmod: '2026-10-20T12:00:00+00:00',
        priority: '0.85'
    },
    {
        loc: 'https://nojomalarab.com/intercity-moving/jeddah-to-makkah/',
        lastmod: '2026-10-20T12:00:00+00:00',
        priority: '0.85'
    },
    {
        loc: 'https://nojomalarab.com/intercity-moving/jeddah-to-madinah/',
        lastmod: '2026-10-20T12:00:00+00:00',
        priority: '0.85'
    },
    {
        loc: 'https://nojomalarab.com/intercity-moving/jeddah-to-taif/',
        lastmod: '2026-10-20T12:00:00+00:00',
        priority: '0.85'
    },
    {
        loc: 'https://nojomalarab.com/intercity-moving/jeddah-to-dammam/',
        lastmod: '2026-10-20T12:00:00+00:00',
        priority: '0.85'
    }
];

let newXmlEntries = '';
for (const entry of newUrls) {
    if (!content.includes(entry.loc)) {
        newXmlEntries += `\n  <url>\n    <loc>${entry.loc}</loc>\n    <lastmod>${entry.lastmod}</lastmod>\n    <priority>${entry.priority}</priority>\n  </url>\n`;
    }
}

if (newXmlEntries) {
    content = content.replace('</urlset>', newXmlEntries + '</urlset>');
    fs.writeFileSync(sitemapPath, content, 'utf8');
    console.log('Successfully updated sitemap.xml with 6 new URLs.');
} else {
    console.log('URLs already present in sitemap.xml.');
}
