import glob
import re

files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.findall(r'<nav[^>]*>[\s\S]*?</nav>', c, re.I)
    # filter for breadcrumb navs (not main header nav)
    bcs = [x for x in m if 'breadcrumb' in x.lower() or ('الرئيسية' in x and len(x) < 1500)]
    if bcs:
        print(f'{filepath}: {len(bcs)} breadcrumbs')
        for b in bcs:
            print('  ', b[:100].replace('\n', ' '))

