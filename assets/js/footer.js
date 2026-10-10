/**
 * Nojom Al Arab - Global Footer Loader
 * Loads the single-source-of-truth footer component into any page containing <div id="site-footer"></div>
 * or ensures the existing footer has the active year updated automatically.
 */
(function() {
    function updateYear() {
        const yearEl = document.getElementById('currentYear');
        if (yearEl) {
            yearEl.textContent = new Date().getFullYear();
        }
    }

    async function loadFooter() {
        const container = document.getElementById('site-footer') || document.getElementById('global-footer-container');
        if (container && !container.innerHTML.trim()) {
            try {
                const response = await fetch('/components/footer.html');
                if (response.ok) {
                    const html = await response.text();
                    container.innerHTML = html;
                    updateYear();
                }
            } catch (err) {
                console.warn('Could not load dynamic footer from /components/footer.html:', err);
            }
        } else {
            updateYear();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadFooter);
    } else {
        loadFooter();
    }
})();
