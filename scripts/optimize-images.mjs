import fs from 'fs';
import path from 'path';
import sharp from 'sharp';

const srcDir = './assets/img/src';
const destDir = './assets/img';

const sizes = [480, 800, 1200];

async function optimizeImages() {
    console.log('=== Starting Image Optimization ===');
    if (!fs.existsSync(srcDir)) {
        console.log('Source directory does not exist:', srcDir);
        return;
    }

    const files = fs.readdirSync(srcDir);
    console.log('Found source files:', files);

    for (const file of files) {
        const ext = path.extname(file).toLowerCase();
        if (!['.jpg', '.jpeg', '.png', '.webp'].includes(ext)) continue;

        const baseName = path.basename(file, ext).toLowerCase().replace(/[^a-z0-9_-]/g, '-');
        const srcPath = path.join(srcDir, file);

        for (const width of sizes) {
            const outName = `${baseName}-${width}.webp`;
            const outPath = path.join(destDir, outName);

            try {
                await sharp(srcPath)
                    .resize({ width, withoutEnlargement: true })
                    .webp({ quality: 80 })
                    .toFile(outPath);

                const stats = fs.statSync(outPath);
                console.log(`Generated: ${outName} (${Math.round(stats.size / 1024)} KB)`);
            } catch (err) {
                console.error(`Error processing ${file} at ${width}px:`, err.message);
            }
        }
    }
    console.log('=== Image Optimization Complete ===');
}

optimizeImages();
