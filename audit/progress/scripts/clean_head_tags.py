import re
from pathlib import Path

html_files = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p)]
cleaned = 0

for p in html_files:
    c = p.read_text(encoding='utf-8')
    orig = c
    
    # 1. Remove single hreflang tag
    c = re.sub(r'\s*<!--\s*6\.1\s*Hreflang[^>]*-->\s*<link\s+rel="alternate"\s+hreflang="ar-SA"[^>]*>', '', c)
    c = re.sub(r'\s*<link\s+rel="alternate"\s+hreflang="ar-SA"[^>]*>', '', c)
    c = re.sub(r'\s*<!--\s*Geo Metadata\s*-->', '', c)
    
    # 2. Ensure theme-color is #0a2540
    if '<meta name="theme-color"' in c:
        c = re.sub(r'<meta\s+name="theme-color"\s+content="[^"]*"', '<meta name="theme-color" content="#0a2540"', c)
    else:
        # inject after viewport
        c = re.sub(r'(<meta\s+name="viewport"[^>]*>)', r'\1\n    <meta name="theme-color" content="#0a2540">', c)
        
    # 3. Ensure og:site_name is unified
    if 'property="og:site_name"' in c:
        c = re.sub(r'<meta\s+property="og:site_name"\s+content="[^"]*"', '<meta property="og:site_name" content="شركة نجوم العرب لنقل الأثاث بجدة"', c)
        
    if c != orig:
        p.write_text(c, encoding='utf-8')
        cleaned += 1

print(f"Cleaned head tags in {cleaned} HTML files.")
