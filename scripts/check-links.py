import os
import re
import urllib.parse

def find_html_files(root_dir='.'):
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        if 'node_modules' in root or '.git' in root or 'dist' in root:
            continue
        for file in files:
            if file.endswith('.html') and not file.endswith('.backup_seo_audit'):
                html_files.append(os.path.normpath(os.path.join(root, file)))
    return sorted(html_files)

def check_link(source_file, url, root_dir='.'):
    # Ignore external, mailto, tel, javascript, fragments, templates, placeholders
    if not url or url.startswith(('mailto:', 'tel:', 'javascript:', '#', 'http://', 'https://', '//', 'wa.me', '${', '{{')):
        return True, None
    if '${' in url or '{{' in url:
        return True, None
    
    # Strip query string and fragment
    clean_url = url.split('#')[0].split('?')[0]
    if not clean_url:
        return True, None
    
    clean_url = urllib.parse.unquote(clean_url)
    
    # Absolute paths relative to domain root
    if clean_url.startswith('/'):
        target_path = os.path.normpath(os.path.join(root_dir, clean_url.lstrip('/')))
    else:
        # Relative path
        source_dir = os.path.dirname(source_file)
        target_path = os.path.normpath(os.path.join(source_dir, clean_url))
        
    # Check if target exists directly (file)
    if os.path.isfile(target_path):
        return True, target_path
    
    # Check if directory with index.html
    if os.path.isdir(target_path):
        index_file = os.path.join(target_path, 'index.html')
        if os.path.isfile(index_file):
            return True, index_file
            
    # Check if target_path + .html exists
    if os.path.isfile(target_path + '.html'):
        return True, target_path + '.html'
        
    # Check if target_path + /index.html exists
    if os.path.isfile(os.path.join(target_path, 'index.html')):
        return True, os.path.join(target_path, 'index.html')
        
    return False, target_path

def main():
    html_files = find_html_files()
    missing_links = []
    total_checked = 0
    
    # Regex to find href and src
    link_regex = re.compile(r'(?:href|src)=["\']([^"\']+)["\']', re.IGNORECASE)
    
    for f in html_files:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
            
        links = link_regex.findall(content)
        for link in links:
            # Skip pure external domains unless pointing to nojomalarab.com
            check_url = link
            if 'nojomalarab.com' in link:
                # normalize to relative path
                parsed = urllib.parse.urlparse(link)
                check_url = parsed.path
                if not check_url:
                    check_url = '/'
                    
            if check_url.startswith(('http://', 'https://')) and 'nojomalarab.com' not in check_url:
                continue
                
            total_checked += 1
            ok, resolved = check_link(f, check_url)
            if not ok:
                missing_links.append({
                    'source': f,
                    'url': link,
                    'resolved_attempt': resolved
                })
                
    print(f"Total internal links/src checked: {total_checked}")
    print(f"Missing count: {len(missing_links)}")
    if missing_links:
        print("\n--- MISSING TARGETS ---")
        for m in missing_links:
            print(f"File: {m['source']} -> Link: {m['url']} (Attempted: {m['resolved_attempt']})")
    else:
        print("ALL INTERNAL LINKS OK - ZERO MISSING")
        
    return missing_links

if __name__ == '__main__':
    main()
