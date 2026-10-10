const fs = require('fs');
let sitemapContent = fs.readFileSync('sitemap.xml', 'utf8');

// Update all <lastmod> entries to 2026-10-06T12:00:00+00:00
// Since all pages received hreflang tags, internal linking fixes, or performance fixes over the last 6 days.
sitemapContent = sitemapContent.replace(/<lastmod>[^<]+<\/lastmod>/g, '<lastmod>2026-10-06T12:00:00+00:00</lastmod>');

fs.writeFileSync('sitemap.xml', sitemapContent);
console.log('Sitemap lastmod updated.');
