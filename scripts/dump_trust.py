with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('=== TRUST-STATS ===')
ts = re.search(r'<section id="trust-stats"[\s\S]*?</section>', text)
if ts: print(ts.group(0))

print('=== TRUST-DETAILS ===')
td = re.search(r'<section id="trust-details"[\s\S]*?</section>', text)
if td: print(td.group(0))

