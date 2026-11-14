import glob
import re

files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html']

for filepath in sorted(files):
    if filepath == 'index.html':
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check visible breadcrumb
    has_visible_bc = bool(re.search(r'aria-label=["\'](?:Breadcrumb|مسار التنقل|خرائط التنقل)["\']|breadcrumb', content, re.I))
    # Check schema breadcrumb
    has_schema_bc = 'BreadcrumbList' in content
    # Check schema webPage / service / etc
    has_webpage = 'WebPage' in content
    # Check movingCompany
    has_moving_company = 'MovingCompany' in content
    
    print(f'{filepath}: visible_bc={has_visible_bc}, schema_bc={has_schema_bc}, webpage={has_webpage}, moving_co={has_moving_company}')

