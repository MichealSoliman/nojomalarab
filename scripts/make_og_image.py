from PIL import Image

# Open the truck photo or team photo and create a 1200x630 landscape banner
source_path = 'assets/img/furniture-moving-truck-jeddah-2.webp'
out_path = 'assets/img/og-image.webp'

with Image.open(source_path) as im:
    # im is 780x1040 (portrait). Let's crop/fit into 1200x630
    target_w, target_h = 1200, 630
    
    # Resize so width fills 1200
    scale = target_w / im.width
    new_w = target_w
    new_h = int(im.height * scale)
    resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Crop center 630 height
    top = (new_h - target_h) // 2
    cropped = resized.crop((0, top, target_w, top + target_h))
    cropped.save(out_path, 'WEBP', quality=90)
    print(f'Successfully created {out_path} with size {cropped.size}')

