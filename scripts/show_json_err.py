import re

with open('about/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

s = re.findall(r'<script\s+type=["\']application/ld\+json["\']>([\s\S]*?)</script>', c)[0]
print("--- Raw ---")
lines = s.splitlines()
for i, l in enumerate(lines[:15]):
    print(f'{i+1}: {l}')

