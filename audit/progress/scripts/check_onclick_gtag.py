import re
from pathlib import Path

html_files = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p)]
onclick_gtag = []

for p in html_files:
    c = p.read_text(encoding='utf-8', errors='ignore')
    if 'gtag(' in c:
        matches = re.findall(r'onclick="[^"]*gtag[^"]*"', c)
        if matches:
            onclick_gtag.append((str(p), len(matches)))

print(f"Files with onclick gtag: {len(onclick_gtag)}")
for f, cnt in onclick_gtag[:10]:
    print(f"  {f}: {cnt}")
