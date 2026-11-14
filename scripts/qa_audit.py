import os
import re
import urllib.parse

def run_qa():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    print('=== 1. PLACEHOLDER CHECK ===')
    placeholders = re.findall(r'\{\{[^}]*\}\}', html)
    print(f'Total {{{{...}}}} placeholders found: {len(placeholders)}')

    print('\n=== 2. H1 & HEADING STRUCTURE CHECK ===')
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.S)
    print(f'Total <h1> count: {len(h1s)}')
    for h in h1s:
        print('H1:', re.sub(r'<[^>]+>', '', h).strip())

    headings = re.findall(r'<(h[1-6])[^>]*>(.*?)</\1>', html, re.S)
    print(f'Total headings (H1-H6): {len(headings)}')
    h_levels = [int(h[0][1]) for h in headings]
    skips = []
    for i in range(len(h_levels) - 1):
        if h_levels[i+1] > h_levels[i] + 1:
            skips.append((h_levels[i], h_levels[i+1], headings[i+1][1].strip()))
    print(f'Heading level jumps: {len(skips)}')
    for s in skips:
        print('   Jump:', s)

    print('\n=== 3. INTERNAL LINKS & SRC CHECK ===')
    # Check all href and src in index.html
    hrefs = re.findall(r'href=["\']([^"\'#][^"\']*)["\']', html)
    srcs = re.findall(r'src=["\']([^"\']+)["\']', html)

    missing_links = []
    for h in set(hrefs):
        if h.startswith('tel:') or h.startswith('https://') or h.startswith('http://'):
            continue
        parsed = urllib.parse.urlparse(h)
        path = parsed.path
        if not path or path == '/':
            continue
        # internal relative or absolute
        clean_path = path.lstrip('/')
        if clean_path.endswith('/'):
            disk_path = clean_path + 'index.html'
        else:
            disk_path = clean_path
        if not os.path.exists(disk_path):
            missing_links.append((h, disk_path))

    for s in set(srcs):
        clean_src = s.lstrip('/')
        if not os.path.exists(clean_src):
            missing_links.append((s, clean_src))

    print(f'Total missing internal links/src: {len(missing_links)}')
    for m in missing_links:
        print('   Missing:', m)

    print('\n=== 4. IMAGE AUDIT (alt, width, height, loading, decoding) ===')
    imgs = re.findall(r'<img[^>]+>', html)
    print(f'Total <img> tags: {len(imgs)}')
    missing_attrs = []
    for img in imgs:
        has_alt = 'alt=' in img and 'alt=""' not in img
        has_w = 'width=' in img
        has_h = 'height=' in img
        has_decoding = 'decoding=' in img
        if not (has_alt and has_w and has_h and has_decoding):
            missing_attrs.append((img[:80], f'alt:{has_alt}, w:{has_w}, h:{has_h}, dec:{has_decoding}'))
    print(f'Images missing critical attributes: {len(missing_attrs)}')
    for ma in missing_attrs:
        print('   ', ma)

    print('\n=== 5. KEYWORD METRICS & STRONG TAGS ===')
    # strip tags for word count
    clean_text = re.sub(r'<script[\s\S]*?</script>', '', html)
    clean_text = re.sub(r'<style[\s\S]*?</style>', '', clean_text)
    clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
    words = clean_text.split()
    total_words = len(words)
    print(f'Total word count in page: {total_words}')

    primary_kw = 'شركة نقل عفش جدة'
    primary_count = html.count(primary_kw)
    print(f'Primary keyword ("{primary_kw}") occurrences: {primary_count} (Density: {(primary_count*4/total_words)*100:.2f}%)')

    synonyms = [
        'نقل عفش جدة',
        'نقل عفش بجدة',
        'شركة نقل عفش بجدة',
        'نقل اثاث جدة',
        'نقل أثاث بجدة',
        'شركة نقل اثاث بجدة',
        'نقل عفش داخل جدة',
        'فك وتركيب وتغليف',
        'سيارات نقل عفش جدة',
        'دينا نقل عفش',
        'ونش رفع عفش جدة',
        'أسعار نقل العفش بجدة'
    ]
    print('\nSynonym occurrences:')
    for syn in synonyms:
        print(f'   - {syn}: {html.count(syn)}')

    strongs = re.findall(r'<strong[^>]*>(.*?)</strong>', html, re.S)
    print(f'\nTotal <strong> occurrences: {len(strongs)}')
    for st in strongs:
        print('   <strong>:', re.sub(r'<[^>]+>', '', st).strip())

    print('\n=== 6. TITLE & DESCRIPTION LENGTH ===')
    title = re.search(r'<title>(.*?)</title>', html, re.S)
    desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.S)
    if title:
        t_str = title.group(1).strip()
        print(f'Title: "{t_str}" (Length: {len(t_str)} chars)')
    if desc:
        d_str = desc.group(1).strip()
        print(f'Description: "{d_str}" (Length: {len(d_str)} chars)')

if __name__ == '__main__':
    run_qa()

