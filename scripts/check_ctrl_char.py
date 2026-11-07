import re

with open('intercity-moving/jeddah-to-riyadh/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

scripts = re.findall(r'<script\s+type=["\']application/ld\+json["\']>([\s\S]*?)</script>', c, re.I)
s = scripts[1]
lines = s.splitlines()
for i, l in enumerate(lines[15:25], start=16):
    print(f'{i}: {repr(l)}')

