import glob
import re
import json

files = glob.glob('*/*.html') + glob.glob('*/*/*.html') + glob.glob('*.html')
script_regex = re.compile(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', re.DOTALL | re.IGNORECASE)

errors = []
total_blocks = 0

for f in files:
    if 'backup' in f: continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    blocks = script_regex.findall(c)
    for idx, b in enumerate(blocks):
        total_blocks += 1
        b_clean = b.strip()
        try:
            parsed = json.loads(b_clean)
        except Exception as e:
            errors.append((f, idx, str(e), b_clean[:100]))

print(f"Total JSON-LD blocks scanned: {total_blocks}")
print(f"Errors found: {len(errors)}")
for err in errors:
    print(err)

