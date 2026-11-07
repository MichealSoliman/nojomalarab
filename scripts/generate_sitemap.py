import glob
import os
import datetime

# Find all valid html files except 404
html_files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html' and f != '404.html']

urls = []
for f in sorted(html_files):
    if f == 'index.html':
        url = 'https://nojomalarab.com/'
        priority = '1.0'
        changefreq = 'weekly'
    elif f.endswith('/index.html'):
        slug = f[:-len('index.html')]
        url = f'https://nojomalarab.com/{slug}'
        if slug.startswith('blogs/'):
            priority = '0.7'
            changefreq = 'monthly'
        elif slug.startswith('areas/'):
            priority = '0.8'
            changefreq = 'monthly'
        else:
            priority = '0.9'
            changefreq = 'weekly'
    else:
        url = f'https://nojomalarab.com/{f}'
        priority = '0.5'
        changefreq = 'monthly'
        
    # get file modification date
    mtime = os.path.getmtime(f)
    lastmod = datetime.datetime.fromtimestamp(mtime, tz=datetime.timezone.utc).strftime('%Y-%m-%d')
    urls.append((url, lastmod, changefreq, priority))

# Generate XML
lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
    '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9',
    '                            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">'
]

for url, lastmod, freq, prio in urls:
    lines.append('  <url>')
    lines.append(f'    <loc>{url}</loc>')
    lines.append(f'    <lastmod>{lastmod}</lastmod>')
    lines.append(f'    <changefreq>{freq}</changefreq>')
    lines.append(f'    <priority>{prio}</priority>')
    lines.append('  </url>')

lines.append('</urlset>')

with open('sitemap.xml', 'w', encoding='utf-8') as out:
    out.write('\n'.join(lines) + '\n')

print(f'Generated sitemap.xml with {len(urls)} URLs.')

