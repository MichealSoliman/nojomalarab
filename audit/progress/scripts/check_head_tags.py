import re
from pathlib import Path

html_files = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p)]
issues = []

for p in html_files:
    c = p.read_text(encoding='utf-8')
    if re.search(r'<meta[^>]+name=["\']keywords["\']', c, re.I):
        issues.append((str(p), 'keywords'))
    if re.search(r'<meta[^>]+(geo\.|icbm)', c, re.I):
        issues.append((str(p), 'geo/icbm'))
    hl = re.findall(r'<link[^>]+hreflang[^>]+>', c)
    if len(hl) == 1:
        issues.append((str(p), f'single hreflang ({len(hl)})'))

print(f"Total head issues found: {len(issues)}")
for f, issue in issues:
    print(f"  {f} -> {issue}")
