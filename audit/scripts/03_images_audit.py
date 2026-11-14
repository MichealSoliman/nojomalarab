import os
import re
import csv
import hashlib
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image

def log(msg):
    with open("audit/run-log.txt", "a", encoding="utf-8") as f:
        f.write(f"[IMAGES-AUDIT] {msg}\n")
    print(msg)

log("Starting images audit...")

html_files = []
for p in Path(".").rglob("*.html"):
    rel = p.as_posix()
    if rel.startswith("audit/") or ".gemini" in rel:
        continue
    html_files.append(p)

images_data = []
file_hashes = {}

# Pre-calculate hashes of assets/img
for img_path in Path("assets/img").rglob("*"):
    if img_path.is_file():
        try:
            with open(img_path, "rb") as f:
                h = hashlib.md5(f.read()).hexdigest()
            file_hashes[img_path.as_posix()] = h
        except Exception:
            pass

for fpath in sorted(html_files):
    rel_page = fpath.as_posix()
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    for img in soup.find_all("img"):
        src = img.get("src", "").strip()
        alt = img.get("alt", "")
        width_attr = img.get("width", "")
        height_attr = img.get("height", "")
        loading = img.get("loading", "")
        decoding = img.get("decoding", "")
        
        # Resolve disk path
        clean_src = src.lstrip("/")
        img_disk = Path(clean_src)
        exists = img_disk.exists() and img_disk.is_file()
        
        file_size_kb = 0.0
        actual_width = None
        actual_height = None
        img_hash = ""
        img_format = ""
        
        if exists:
            file_size_kb = round(img_disk.stat().st_size / 1024, 2)
            img_hash = file_hashes.get(img_disk.as_posix(), "")
            try:
                with Image.open(img_disk) as im:
                    actual_width, actual_height = im.size
                    img_format = im.format
            except Exception as e:
                img_format = "CORRUPT_OR_UNKNOWN"
                
        # Issues check
        issues = []
        if not exists:
            issues.append("FILE_NOT_FOUND_404")
        if not alt.strip():
            issues.append("MISSING_ALT")
        if not width_attr or not height_attr:
            issues.append("MISSING_DIMENSIONS")
        if loading != "lazy" and "logo" not in src.lower() and "hero" not in src.lower():
            issues.append("NON_LAZY_LOADING")
        if file_size_kb > 200:
            issues.append("HEAVY_IMAGE_OVER_200KB")
        if img_format and img_format.lower() not in ["webp", "svg", "avif"]:
            issues.append(f"LEGACY_FORMAT_{img_format}")
            
        images_data.append({
            "page": rel_page,
            "src": src,
            "exists": exists,
            "alt": alt,
            "width_attr": width_attr,
            "height_attr": height_attr,
            "actual_dimensions": f"{actual_width}x{actual_height}" if actual_width else "N/A",
            "file_size_kb": file_size_kb,
            "format": img_format,
            "loading": loading,
            "decoding": decoding,
            "md5_hash": img_hash,
            "issues": ";".join(issues) if issues else "OK"
        })

with open("audit/06-images.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=images_data[0].keys())
    writer.writeheader()
    writer.writerows(images_data)

log(f"Images audit finished. {len(images_data)} image tags evaluated.")

