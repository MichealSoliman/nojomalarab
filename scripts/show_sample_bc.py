import re

with open('areas/furniture-moving-hayu-alhamdaniyah/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

bc = re.search(r'<nav[^>]*aria-label=["\']Breadcrumb["\'][^>]*>([\s\S]*?)</nav>', c, re.I)
if bc:
    print('Found nav:\n', bc.group(0))

schemas = re.findall(r'<script\s+type=["\']application/ld\+json["\']>([\s\S]*?)</script>', c, re.I)
for s in schemas:
    if 'BreadcrumbList' in s:
        print('BreadcrumbList Schema:\n', s)

