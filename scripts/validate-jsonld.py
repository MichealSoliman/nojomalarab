import os
import re
import json

def validate_jsonld():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Check for any remaining {{ or }} in the entire file
    placeholders = re.findall(r'\{\{[^}]*\}\}', html)
    if placeholders:
        print(f'[FAIL] Found {len(placeholders)} placeholders in index.html:')
        for p in placeholders[:10]:
            print(f'   {p}')
        return False
    else:
        print('[PASS] Zero placeholders {{...}} found in index.html')

    # 2. Extract and parse all JSON-LD blocks
    scripts = re.findall(r'<script\s+type=["\']application/ld\+json["\']>([\s\S]*?)</script>', html, re.I)
    if not scripts:
        print('[FAIL] No JSON-LD scripts found!')
        return False

    print(f'[INFO] Found {len(scripts)} JSON-LD script block(s)')

    for i, s in enumerate(scripts):
        try:
            data = json.loads(s)
            print(f'[PASS] Script block {i+1} parsed valid JSON successfully.')
        except Exception as e:
            print(f'[FAIL] Script block {i+1} JSON parse error: {e}')
            return False

        # Recursively check for empty strings or null values
        def check_clean(obj, path=''):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    subpath = f'{path}.{k}' if path else k
                    if v is None:
                        print(f'[FAIL] Null value at {subpath}')
                        return False
                    if isinstance(v, str) and len(v.strip()) == 0:
                        print(f'[FAIL] Empty string at {subpath}')
                        return False
                    if not check_clean(v, subpath):
                        return False
            elif isinstance(obj, list):
                for idx, item in enumerate(obj):
                    subpath = f'{path}[{idx}]'
                    if item is None:
                        print(f'[FAIL] Null value at {subpath}')
                        return False
                    if isinstance(item, str) and len(item.strip()) == 0:
                        print(f'[FAIL] Empty string at {subpath}')
                        return False
                    if not check_clean(item, subpath):
                        return False
            return True

        if not check_clean(data):
            return False
        print(f'[PASS] Script block {i+1} contains no nulls or empty strings.')

    return True

if __name__ == '__main__':
    success = validate_jsonld()
    if not success:
        exit(1)

