import glob
import re

files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git')]

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    orig = c
    
    # Check images
    def fix_img(m):
        tag = m.group(0)
        # if not hero or first image, add loading="lazy" and decoding="async"
        if 'loading=' not in tag and 'hero' not in tag.lower():
            tag = tag[:-1].strip() + ' loading="lazy" decoding="async">'
        # if width not in tag, add default width/height if it's a known image or placeholder
        if 'width=' not in tag:
            if 'og-image' in tag or 'work' in tag or 'truck' in tag or 'team' in tag or 'pack' in tag:
                tag = tag[:-1].strip() + ' width="800" height="533">'
            elif 'logo' in tag:
                tag = tag[:-1].strip() + ' width="64" height="64">'
        return tag
        
    c = re.sub(r'<img[^>]+>', fix_img, c)
    if c != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f'Optimized images in {f}')

