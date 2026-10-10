const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');

function getAllHtmlFiles(dir, fileList = []) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            if (file === 'node_modules' || file === '.git' || file === 'dist' || file === 'components') continue;
            getAllHtmlFiles(fullPath, fileList);
        } else if (file.endsWith('.html')) {
            fileList.push(fullPath);
        }
    }
    return fileList;
}

const htmlFiles = getAllHtmlFiles(rootDir);
let updatedCount = 0;

for (const file of htmlFiles) {
    let content = fs.readFileSync(file, 'utf8');

    // Skip 404.html if it's just a simple modal
    const relPath = path.relative(rootDir, file);
    if (relPath === '404.html') {
        console.log(`[SKIPPED] ${relPath}`);
        continue;
    }

    // Match footer block including any preceding comment
    const footerRegex = /(?:<!--\s*(?:Footer|========== GLOBAL MEGA FOOTER COMPONENT)[\s\S]*?-->\s*)?<footer[\s\S]*?<\/footer>/i;

    if (footerRegex.test(content)) {
        content = content.replace(footerRegex, `    <!-- Global Footer Component (Loaded from /components/footer.html) -->\n    <div id="site-footer"></div>`);

        // Ensure assets/js/footer.js is loaded
        if (!content.includes('assets/js/footer.js')) {
            content = content.replace('</body>', '    <script src="/assets/js/footer.js" defer></script>\n</body>');
        }

        fs.writeFileSync(file, content, 'utf8');
        console.log(`[UPDATED TO DYNAMIC COMPONENT] ${relPath}`);
        updatedCount++;
    } else if (content.includes('id="site-footer"') || content.includes("id='site-footer'")) {
        if (!content.includes('assets/js/footer.js')) {
            content = content.replace('</body>', '    <script src="/assets/js/footer.js" defer></script>\n</body>');
            fs.writeFileSync(file, content, 'utf8');
        }
        console.log(`[ALREADY DYNAMIC] ${relPath}`);
        updatedCount++;
    } else {
        console.log(`[NO FOOTER PATTERN] ${relPath}`);
    }
}

console.log(`\n✨ Successfully converted ${updatedCount} pages to use the standalone dynamic footer component!`);
