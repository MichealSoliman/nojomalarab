import os
import glob
import re

# 1. Fix in best-furniture-moving-company-jeddah/index.html
best_file = 'best-furniture-moving-company-jeddah/index.html'
if os.path.exists(best_file):
    with open(best_file, 'r', encoding='utf-8') as fp:
        c = fp.read()
    c = c.replace('https://nojomalarab.com/moving-prices-in-jeddah/', 'https://nojomalarab.com/furniture-moving-prices-jeddah/')
    c = c.replace('/moving-prices-in-jeddah/', '/furniture-moving-prices-jeddah/')
    c = c.replace('https://nojomalarab.com/furniture-moving-inside-jeddah/', 'https://nojomalarab.com/areas/')
    c = c.replace('/furniture-moving-inside-jeddah/', '/areas/')
    c = c.replace('https://nojomalarab.com/services/bedroom-moving-jeddah/', 'https://nojomalarab.com/furniture-disassembly-and-reassembly-in-jeddah/')
    c = c.replace('/services/bedroom-moving-jeddah/', '/furniture-disassembly-and-reassembly-in-jeddah/')
    c = c.replace('https://nojomalarab.com/furniture-company-jeddah/', 'https://nojomalarab.com/')
    c = c.replace('/furniture-company-jeddah/', '/')
    c = c.replace('https://nojomalarab.com/blog/the-best-way-to-transport-electrical-appliances/', 'https://nojomalarab.com/blogs/packing-fragile-electronics-glass-antiques/')
    c = c.replace('/blog/the-best-way-to-transport-electrical-appliances/', '/blogs/packing-fragile-electronics-glass-antiques/')
    with open(best_file, 'w', encoding='utf-8') as fp:
        fp.write(c)
    print("Fixed known broken links in best-furniture-moving-company-jeddah")

# 2. Fix affordable-furniture-moving-jeddah
aff_file = 'affordable-furniture-moving-jeddah/index.html'
if os.path.exists(aff_file):
    with open(aff_file, 'r', encoding='utf-8') as fp:
        c = fp.read()
    c = c.replace('https://nojomalarab.com/apartment-moving-jeddah/', 'https://nojomalarab.com/apartment-furniture-moving-jeddah/')
    c = c.replace('/apartment-moving-jeddah/', '/apartment-furniture-moving-jeddah/')
    with open(aff_file, 'w', encoding='utf-8') as fp:
        fp.write(c)
    print("Fixed apartment-moving-jeddah in affordable-furniture-moving-jeddah")

# 3. Fix dina transport link in neighborhood pages
for d_file in glob.glob('areas/*/index.html'):
    with open(d_file, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'furniture-dina-transport-jeddah' in c:
        c = c.replace('https://nojomalarab.com/furniture-dina-transport-jeddah/', 'https://nojomalarab.com/furniture-transport-trucks-in-jeddah/')
        c = c.replace('/furniture-dina-transport-jeddah/', '/furniture-transport-trucks-in-jeddah/')
        with open(d_file, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f"Fixed dina link in {d_file}")

# 4. Fix self canonical & og:url in hayu-al-safa and hayu-alshati
safa_file = 'areas/furniture-moving-hayu-al-safa/index.html'
if os.path.exists(safa_file):
    with open(safa_file, 'r', encoding='utf-8') as fp:
        c = fp.read()
    c = c.replace('https://nojomalarab.com/furniture-moving-hayu-al-safa/', 'https://nojomalarab.com/areas/furniture-moving-hayu-al-safa/')
    with open(safa_file, 'w', encoding='utf-8') as fp:
        fp.write(c)
    print("Fixed canonical/og:url in safa")

shati_file = 'areas/furniture-moving-in-hayu-alshati-jeddah/index.html'
if os.path.exists(shati_file):
    with open(shati_file, 'r', encoding='utf-8') as fp:
        c = fp.read()
    c = c.replace('https://nojomalarab.com/furniture-moving-in-hayu-alshati-jeddah/', 'https://nojomalarab.com/areas/furniture-moving-in-hayu-alshati-jeddah/')
    with open(shati_file, 'w', encoding='utf-8') as fp:
        fp.write(c)
    print("Fixed canonical/og:url in shati")

print("All broken links corrected.")
