import os
import glob
import re
import csv

def process_files():
    html_files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html']
    
    # Junk tags patterns to remove
    junk_patterns = [
        r'\s*<meta\s+name=["\']keywords["\'][^>]*>',
        r'\s*<meta\s+name=["\']geo\.region["\'][^>]*>',
        r'\s*<meta\s+name=["\']geo\.placename["\'][^>]*>',
        r'\s*<meta\s+name=["\']geo\.position["\'][^>]*>',
        r'\s*<meta\s+name=["\']ICBM["\'][^>]*>',
        r'\s*<meta\s+name=["\']revisit-after["\'][^>]*>',
        r'\s*<meta\s+name=["\']distribution["\'][^>]*>',
        r'\s*<meta\s+name=["\']rating["\'][^>]*>',
        r'\s*<meta\s+name=["\']language["\'][^>]*>',
        r'\s*<meta\s+name=["\']bingbot["\'][^>]*>',
        r'\s*<meta\s+name=["\']color-scheme["\'][^>]*>',
    ]
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig_content = content
        
        # 1. Remove junk tags
        for pat in junk_patterns:
            content = re.sub(pat, '', content, flags=re.I)
            
        # 2. Standardize theme-color
        if '<meta name="theme-color"' in content:
            content = re.sub(r'<meta\s+name=["\']theme-color["\'][^>]*>', '<meta name="theme-color" content="#0a2540">', content, flags=re.I)
        else:
            # Insert after viewport if possible
            content = re.sub(r'(<meta\s+name=["\']viewport["\'][^>]*>)', r'\1\n    <meta name="theme-color" content="#0a2540">', content, flags=re.I)

        # 3. Standardize og:site_name
        if 'og:site_name' in content:
            content = re.sub(r'<meta\s+property=["\']og:site_name["\'][^>]*>', '<meta property="og:site_name" content="شركة نجوم العرب لنقل الأثاث بجدة">', content, flags=re.I)
            
        # 4. Standardize og:image default if it's using logo.webp or unoptimized
        # If og:image is present, make sure width, height, and type are present
        # Replace logo.webp with {{og-image.webp}}
        content = re.sub(r'https://nojomalarab\.com/assets/img/logo\.webp', 'https://nojomalarab.com/assets/img/{{og-image.webp}}', content)
        
        # Add og:image:width, height, type if og:image exists and they don't
        if 'property="og:image"' in content or "property='og:image'" in content:
            if 'og:image:width' not in content:
                content = re.sub(r'(<meta\s+property=["\']og:image["\'][^>]*>)', r'\1\n    <meta property="og:image:width" content="1200">\n    <meta property="og:image:height" content="630">\n    <meta property="og:image:type" content="image/webp">', content, flags=re.I)

        # 5. Standardize tel:0500504024 to tel:+966500504024
        content = re.sub(r'tel:0500504024', 'tel:+966500504024', content)
        
        # 6. Check contact/index.html google maps embed
        if filepath == 'contact/index.html':
            # Replace Riyadh embed iframe with {{رابط GBP الحقيقي}}
            content = re.sub(
                r'<iframe\s+src="https://www\.google\.com/maps/embed\?pb=[^"]+"[^>]*>\s*</iframe>',
                r'<iframe src="{{رابط GBP الحقيقي}}" width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" class="w-full rounded-xl"></iframe>',
                content
            )

        # 7. Check canonical consistency
        # Determine expected canonical for file
        if filepath == 'index.html':
            expected_url = 'https://nojomalarab.com/'
        elif filepath == '404.html':
            expected_url = 'https://nojomalarab.com/404.html'
        elif filepath == 'privacy-policy.html':
            expected_url = 'https://nojomalarab.com/privacy-policy.html'
        elif filepath == 'terms.html':
            expected_url = 'https://nojomalarab.com/terms.html'
        elif filepath.endswith('/index.html'):
            slug = filepath[:-len('index.html')]
            expected_url = f'https://nojomalarab.com/{slug}'
        else:
            expected_url = f'https://nojomalarab.com/{filepath}'
            
        # Update or verify canonical tag
        if '<link rel="canonical"' in content or "<link rel='canonical'" in content:
            content = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\'][^"\']+["\']\s*/?>', f'<link rel="canonical" href="{expected_url}">', content, flags=re.I)
        else:
            # insert before </head>
            content = content.replace('</head>', f'    <link rel="canonical" href="{expected_url}">\n</head>')

        if content != orig_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {filepath}')

    # Also update components/footer.html if it has tel:0500504024
    if os.path.exists('components/footer.html'):
        with open('components/footer.html', 'r', encoding='utf-8') as f:
            fc = f.read()
        nfc = re.sub(r'tel:0500504024', 'tel:+966500504024', fc)
        if nfc != fc:
            with open('components/footer.html', 'w', encoding='utf-8') as f:
                f.write(nfc)
            print('Updated components/footer.html tel')

def generate_pages_audit():
    html_files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html']
    
    rows = []
    for filepath in sorted(html_files):
        with open(filepath, 'r', encoding='utf-8') as fp:
            c = fp.read()
        head = re.search(r'<head>([\s\S]*?)</head>', c, re.I)
        h = head.group(1) if head else ''
        
        t = re.search(r'<title>(.*?)</title>', h, re.I | re.S)
        t_text = t.group(1).strip() if t else 'MISSING'
        
        d = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', h, re.I | re.S)
        d_text = d.group(1).strip() if d else 'MISSING'
        
        h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.I | re.S)
        h1_text = ' | '.join(re.sub(r'<[^>]+>', '', x).strip() for x in h1s) if h1s else 'MISSING'
        h1_count = len(h1s)
        
        can = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', h, re.I)
        can_url = can.group(1).strip() if can else 'MISSING'
        
        og_img = re.search(r'<meta\s+property=["\']og:image["\']\s+content=["\'](.*?)["\']', h, re.I)
        og_img_url = og_img.group(1).strip() if og_img else 'MISSING'
        
        # page url
        if filepath == 'index.html': page_url = 'https://nojomalarab.com/'
        elif filepath.endswith('/index.html'): page_url = f"https://nojomalarab.com/{filepath[:-len('index.html')]}"
        else: page_url = f"https://nojomalarab.com/{filepath}"
        
        rows.append({
            'url': page_url,
            'title': t_text,
            'title_len': len(t_text),
            'description': d_text,
            'desc_len': len(d_text),
            'h1': h1_text,
            'h1_count': h1_count,
            'canonical': can_url,
            'og_image': og_img_url
        })
        
    with open('pages-audit.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
        fieldnames = ['url', 'title', 'title_len', 'description', 'desc_len', 'h1', 'h1_count', 'canonical', 'og_image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f'Generated pages-audit.csv with {len(rows)} pages.')

if __name__ == '__main__':
    process_files()
    generate_pages_audit()

