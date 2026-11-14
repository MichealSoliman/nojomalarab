import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script\s+type=["\']application/ld\+json["\']>([\s\S]*?)</script>', text, re.I)
print(f'Total ld+json scripts: {len(scripts)}')
for i, s in enumerate(scripts):
    print(f'=== Script {i+1} ===')
    print(s[:400])

