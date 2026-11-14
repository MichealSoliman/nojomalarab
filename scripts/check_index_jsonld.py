import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

s = re.findall(r'<script\s+type=["\']application/ld\+json["\']>([\s\S]*?)</script>', c)[0]
lines = s.splitlines()
for i in range(25, 36):
    print(f'{i+1}: {lines[i]}')

