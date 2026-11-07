import os
import glob
import re

files = [f.replace('\\', '/') for f in glob.glob('**/*.html', recursive=True) if not f.startswith('.git') and f != 'components/footer.html']

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    head = re.search(r'<head>([\s\S]*?)</head>', c, re.I)
    if not head:
        continue
    h = head.group(1)
    
    t = re.search(r'<title>(.*?)</title>', h, re.I | re.S)
    t_text = t.group(1).strip() if t else 'MISSING'
    
    d = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', h, re.I | re.S)
    d_text = d.group(1).strip() if d else 'MISSING'
    
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.I | re.S)
    h1_text = ' | '.join(re.sub(r'<[^>]+>', '', x).strip() for x in h1s) if h1s else 'MISSING'
    
    print(f'{f} | T_len={len(t_text)} | D_len={len(d_text)} | H1_cnt={len(h1s)}')
    if len(h1s) != 1:
        print(f'   H1 issue in {f}: count={len(h1s)}')

