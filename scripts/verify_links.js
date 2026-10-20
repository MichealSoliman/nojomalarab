const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');

const testFiles = [
  'index.html',
  'intercity-furniture-moving-from-jeddah/index.html',
  'intercity-moving/index.html',
  'intercity-moving/jeddah-to-riyadh/index.html',
  'intercity-moving/jeddah-to-makkah/index.html',
  'intercity-moving/jeddah-to-madinah/index.html',
  'intercity-moving/jeddah-to-taif/index.html',
  'intercity-moving/jeddah-to-dammam/index.html',
  'components/footer.html'
];

let totalChecks = 0;
let errors = [];

for (const relFile of testFiles) {
  const filePath = path.join(rootDir, relFile);
  if (!fs.existsSync(filePath)) {
    errors.push(`File missing: ${relFile}`);
    continue;
  }

  const content = fs.readFileSync(filePath, 'utf8');
  const fileDir = path.dirname(filePath);

  // Match href="..."
  const matches = [...content.matchAll(/href=["']([^"']+)["']/g)];
  for (const match of matches) {
    const rawHref = match[1];

    // Ignore anchors, tel, mailto, javascript, external http(s)
    if (
      rawHref.startsWith('#') ||
      rawHref.startsWith('tel:') ||
      rawHref.startsWith('mailto:') ||
      rawHref.startsWith('javascript:') ||
      rawHref.startsWith('http://') ||
      rawHref.startsWith('https://')
    ) {
      continue;
    }

    totalChecks++;
    // Clean query/hash
    const cleanHref = rawHref.split('?')[0].split('#')[0];
    if (!cleanHref) continue;

    let targetPath;
    if (cleanHref.startsWith('/')) {
      targetPath = path.join(rootDir, cleanHref);
    } else {
      targetPath = path.resolve(fileDir, cleanHref);
    }

    // If target is directory or ends in '/', check if index.html exists
    let exists = false;
    if (fs.existsSync(targetPath)) {
      const stat = fs.statSync(targetPath);
      if (stat.isDirectory()) {
        if (fs.existsSync(path.join(targetPath, 'index.html'))) {
          exists = true;
        }
      } else {
        exists = true;
      }
    } else {
      // Maybe cleanHref didn't have index.html e.g. ../something
      if (fs.existsSync(targetPath + '.html')) {
        exists = true;
      } else if (fs.existsSync(path.join(targetPath, 'index.html'))) {
        exists = true;
      }
    }

    if (!exists) {
      errors.push(`Broken link in [${relFile}]: href="${rawHref}" -> resolved to "${targetPath}"`);
    }
  }
}

console.log(`Validation complete: Checked ${totalChecks} internal links across ${testFiles.length} files.`);
if (errors.length > 0) {
  console.error(`Found ${errors.length} errors:`);
  errors.forEach(e => console.error(' - ' + e));
  process.exit(1);
} else {
  console.log('ALL INTERNAL LINKS ARE VALID! No broken links found.');
}
