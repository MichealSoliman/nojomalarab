import re
from pathlib import Path

# 1. Fix carpenter
p1 = Path('carpenter-furniture-disassembly-assembly-jeddah/index.html')
c1 = p1.read_text(encoding='utf-8')
c1_fixed = c1.replace('{{ضمانات حقيقية}}', 'عناية فائقة وتعهد بالسلامة')
p1.write_text(c1_fixed, encoding='utf-8')
print('Fixed carpenter placeholders')

# 2. Fix intercity
p2 = Path('intercity-furniture-moving-from-jeddah/index.html')
c2 = p2.read_text(encoding='utf-8')
c2_fixed = c2.replace('{{ضمانات حقيقية}}', 'عناية فائقة وتعهد بالسلامة')
p2.write_text(c2_fixed, encoding='utf-8')
print('Fixed intercity placeholders')

# 3. Fix prices og-image
p3 = Path('furniture-moving-prices-jeddah/index.html')
c3 = p3.read_text(encoding='utf-8')
c3_fixed = c3.replace('{{og-default.webp}}', 'og-image.webp')
p3.write_text(c3_fixed, encoding='utf-8')
print('Fixed prices og-image placeholder')

# 4. Fix contact GBP iframe
p4 = Path('contact/index.html')
c4 = p4.read_text(encoding='utf-8')
c4_fixed = re.sub(r'<!-- خريطة جوجل مصغرة -->\s*<div class="mt-12">[\s\S]*?</div>\s*</div>', '', c4)
p4.write_text(c4_fixed, encoding='utf-8')
print('Fixed contact GBP placeholder')
