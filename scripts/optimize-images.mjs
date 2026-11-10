import fs from 'fs';
import path from 'path';
import sharp from 'sharp';

const srcDir = './assets/img/src';
const destDir = './assets/img';

if (!fs.existsSync(srcDir)) {
  fs.mkdirSync(srcDir, { recursive: true });
}

console.log('--- Starting Image Optimization (Sharp) ---');

async function processImages() {
  const report = [];

  // 1. Hero Image: 1200x900 (primary), 768x576, 480x360
  const heroSrc = fs.existsSync(path.join(srcDir, 'hero.webp'))
    ? path.join(srcDir, 'hero.webp')
    : path.join(destDir, 'furniture-moving-in-jeddah.webp');

  if (fs.existsSync(heroSrc)) {
    const srcSize = fs.statSync(heroSrc).size;

    // 1200x900
    await sharp(heroSrc)
      .resize(1200, 900, { fit: 'cover' })
      .webp({ quality: 80 })
      .toFile(path.join(destDir, 'hero-1200.webp'));
    report.push({
      file: 'hero-1200.webp',
      dim: '1200x900',
      before: srcSize,
      after: fs.statSync(path.join(destDir, 'hero-1200.webp')).size
    });

    // 768x576
    await sharp(heroSrc)
      .resize(768, 576, { fit: 'cover' })
      .webp({ quality: 80 })
      .toFile(path.join(destDir, 'hero-768.webp'));
    report.push({
      file: 'hero-768.webp',
      dim: '768x576',
      before: srcSize,
      after: fs.statSync(path.join(destDir, 'hero-768.webp')).size
    });

    // 480x360
    await sharp(heroSrc)
      .resize(480, 360, { fit: 'cover' })
      .webp({ quality: 80 })
      .toFile(path.join(destDir, 'hero-480.webp'));
    report.push({
      file: 'hero-480.webp',
      dim: '480x360',
      before: srcSize,
      after: fs.statSync(path.join(destDir, 'hero-480.webp')).size
    });
  }

  // 2. Open Graph Image: 1200x630
  const ogSrc = fs.existsSync(path.join(srcDir, 'work-2.jpg'))
    ? path.join(srcDir, 'work-2.jpg')
    : heroSrc;

  if (fs.existsSync(ogSrc)) {
    const srcSize = fs.statSync(ogSrc).size;
    await sharp(ogSrc)
      .resize(1200, 630, { fit: 'cover' })
      .webp({ quality: 85 })
      .toFile(path.join(destDir, 'og-image.webp'));
    report.push({
      file: 'og-image.webp',
      dim: '1200x630',
      before: srcSize,
      after: fs.statSync(path.join(destDir, 'og-image.webp')).size
    });
  }

  // 3. Logo: 512x512 and 128x128
  const logoSrc = fs.existsSync(path.join(srcDir, 'logo.webp'))
    ? path.join(srcDir, 'logo.webp')
    : path.join(destDir, 'logo.webp');

  if (fs.existsSync(logoSrc)) {
    const srcSize = fs.statSync(logoSrc).size;
    await sharp(logoSrc)
      .resize(512, 512, { fit: 'contain', background: { r: 255, g: 255, b: 255, alpha: 0 } })
      .webp({ quality: 90 })
      .toFile(path.join(destDir, 'logo-512.webp'));
    report.push({
      file: 'logo-512.webp',
      dim: '512x512',
      before: srcSize,
      after: fs.statSync(path.join(destDir, 'logo-512.webp')).size
    });

    await sharp(logoSrc)
      .resize(128, 128, { fit: 'contain', background: { r: 255, g: 255, b: 255, alpha: 0 } })
      .webp({ quality: 90 })
      .toFile(path.join(destDir, 'logo-128.webp'));
    report.push({
      file: 'logo-128.webp',
      dim: '128x128',
      before: srcSize,
      after: fs.statSync(path.join(destDir, 'logo-128.webp')).size
    });
  }

  // 4. Gallery Images (6 real work photos): 800x600 and 480x360
  const galleryItems = [
    { src: 'work-1.jpg', name: 'furniture-packaging-jeddah-1', title: 'تغليف وتجهيز الأثاث' },
    { src: 'work-2.jpg', name: 'furniture-moving-truck-jeddah-2', title: 'سيارات نقل عفش مجهزة' },
    { src: 'work-3.jpg', name: 'furniture-disassembly-jeddah-3', title: 'فك غرف النوم والقطع الخشبية' },
    { src: 'work-4.jpg', name: 'furniture-loading-jeddah-4', title: 'ترتيب وتحميل العفش بالسيارة' },
    { src: 'work-5.jpg', name: 'fragile-items-protection-jeddah-5', title: 'حماية الزجاج والأجهزة الحساسة' },
    { src: 'work-6.jpg', name: 'moving-team-jeddah-6', title: 'فريق العمل أثناء النقل' }
  ];

  for (const item of galleryItems) {
    const itemSrc = path.join(srcDir, item.src);
    if (fs.existsSync(itemSrc)) {
      const srcSize = fs.statSync(itemSrc).size;

      // 800x600
      const out800 = path.join(destDir, `${item.name}.webp`);
      await sharp(itemSrc)
        .resize(800, 600, { fit: 'cover' })
        .webp({ quality: 80 })
        .toFile(out800);
      report.push({
        file: `${item.name}.webp`,
        dim: '800x600',
        before: srcSize,
        after: fs.statSync(out800).size
      });

      // 480x360
      const out480 = path.join(destDir, `${item.name}-480.webp`);
      await sharp(itemSrc)
        .resize(480, 360, { fit: 'cover' })
        .webp({ quality: 80 })
        .toFile(out480);
      report.push({
        file: `${item.name}-480.webp`,
        dim: '480x360',
        before: srcSize,
        after: fs.statSync(out480).size
      });
    }
  }

  // Print Table
  console.log('\n--- Image Optimization Report ---');
  console.table(report.map(r => ({
    File: r.file,
    Dimensions: r.dim,
    'Before (KB)': (r.before / 1024).toFixed(1),
    'After (KB)': (r.after / 1024).toFixed(1),
    'Reduction': `${(100 - (r.after / r.before) * 100).toFixed(1)}%`
  })));
}

processImages().catch(err => {
  console.error('Error during image processing:', err);
  process.exit(1);
});

