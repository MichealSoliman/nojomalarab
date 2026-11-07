import glob
import re
import json

files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html']

for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    scripts = re.findall(r'<script\s+type=["\']application/ld\+json["\']>([\s\S]*?)</script>', content, re.I)
    for i, s in enumerate(scripts):
        # replace template placeholders temporarily to test JSON validity
        cleaned = re.sub(r'\{\{[^}]+\}\}', '"PLACEHOLDER"', s)
        try:
            data = json.loads(cleaned)
        except Exception as e:
            print(f'JSON ERROR in {filepath} [block {i}]: {e}')

