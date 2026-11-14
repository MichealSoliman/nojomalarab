import glob

files = glob.glob('*/*.html') + glob.glob('*/*/*.html') + glob.glob('*.html')
junk = ['geo.placename', 'geo.region', 'geo.position', 'ICBM', 'revisit-after', 'distribution', 'rating', 'bingbot', 'color-scheme', 'name="keywords"']

found = 0
for f in files:
    if 'backup' in f or f == 'index.html':
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    has_any = []
    for j in junk:
        if j in c:
            has_any.append(j)
    if has_any:
        print(f"{f}: {has_any}")
        found += 1
print(f"Total files with junk meta tags: {found}")

