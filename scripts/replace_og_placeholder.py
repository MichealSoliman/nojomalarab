import glob

files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git')]

updated = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if '{{og-image.webp}}' in c:
        c = c.replace('{{og-image.webp}}', 'og-image.webp')
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        updated += 1

print(f'Updated {updated} files replacing {{{{og-image.webp}}}} with real og-image.webp')

