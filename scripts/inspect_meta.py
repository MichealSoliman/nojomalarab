import os
import glob
import re

files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html']

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Check maps
    maps = re.findall(r'https?://(?:maps\.google\.com|www\.google\.com/maps)[^"\'\s<>]+', c)
    if maps:
        print(f'{f} has google maps links: {len(maps)}')
        for m in maps[:2]:
            print('   ', m[:100])

