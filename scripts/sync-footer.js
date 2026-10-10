const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');
const componentPath = path.join(rootDir, 'components', 'footer.html');

if (!fs.existsSync(componentPath)) {
    console.error(`[ERROR] Component file not found at: ${componentPath}`);
    process.exit(1);
}

const footerHtml = fs.readFileSync(componentPath, 'utf8').trim();

function getHtmlFiles(dir) {
    let results = [];
    const list = fs.readdirSync(dir, { withFileTypes: true });
    for (const item of list) {
        if (item.name === 'node_modules' || item.name === '.git' || item.name === '.agents' || item.name === 'components') continue;
        const fullPath = path.join(dir, item.name);
        if (item.isDirectory()) {
            results = results.concat(getHtmlFiles(fullPath));
        } else if (item.name.endsWith('.html')) {
            results.push(fullPath);
        }
    }
    return results;
}

const htmlFiles = getHtmlFiles(rootDir);
let updatedCount = 0;

const footerRegex = /<!-- ========== (?:GLOBAL MEGA )?FOOTER (?:COMPONENT )?========== -->[\s\S]*?<\/footer>|<footer[\s\S]*?<\/footer>/i;

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    if (footerRegex.test(content)) {
        content = content.replace(footerRegex, footerHtml);
        
        // Ensure footer.js script is included if not present
        if (!content.includes('/assets/js/footer.js') && !content.includes('assets/js/footer.js')) {
            if (content.includes('</body>')) {
                content = content.replace('</body>', '    <script src="/assets/js/footer.js" defer></script>\n</body>');
            }
        }
        
        fs.writeFileSync(file, content, 'utf8');
        updatedCount++;
        console.log(`[UPDATED] ${path.relative(rootDir, file)}`);
    } else {
        console.warn(`[SKIPPED - NO FOOTER FOUND] ${path.relative(rootDir, file)}`);
    }
});

console.log(`\n🎉 Successfully synced footer across ${updatedCount} HTML files!`);
