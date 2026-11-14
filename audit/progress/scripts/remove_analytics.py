import re
from pathlib import Path

html_files = [p for p in Path('.').rglob('*.html') if not str(p).startswith('audit') and '.gemini' not in str(p)]
modified_files = []

for p in html_files:
    content = p.read_text(encoding='utf-8')
    orig = content
    
    # 1. Remove google tag manager script tag
    content = re.sub(r'\s*<!--\s*Google tag\s*\(gtag\.js\)\s*-->\s*<script\s+async\s+src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>', '', content)
    
    # 2. Remove window.dataLayer / gtag config script block
    content = re.sub(r'\s*<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];\s*function\s+gtag\(\)\{dataLayer\.push\(arguments\);\}\s*gtag\(\'js\',\s*new\s+Date\(\)\);\s*gtag\(\'config\',\s*\'[^\']+\'\);\s*</script>', '', content)
    
    # 3. Remove analytics.js script tag
    content = re.sub(r'\s*<!--\s*\d+\.\s*Analytics Script\s*-->\s*<script\s+src="[^"]*analytics\.js"[^>]*></script>', '', content)
    content = re.sub(r'\s*<script\s+src="[^"]*analytics\.js"[^>]*></script>', '', content)
    
    if content != orig:
        p.write_text(content, encoding='utf-8')
        modified_files.append(p.as_posix())

print(f"Removed Google Analytics / gtag / analytics.js from {len(modified_files)} files.")
