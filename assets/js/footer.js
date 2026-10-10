/**
 * Nojom Al Arab - Global Footer Dynamic Component Loader
 * Automatically fetches and injects /components/footer.html into #site-footer on every page.
 * Editing /components/footer.html once updates the footer everywhere instantly!
 */
(function () {
    function updateYear(container) {
        var yearEl = (container || document).querySelector('#currentYear');
        if (yearEl) {
            yearEl.textContent = new Date().getFullYear();
        }
    }

    async function loadFooter() {
        var target = document.getElementById('site-footer') || 
                     document.getElementById('global-footer') || 
                     document.getElementById('global-site-footer');

        if (!target) return;

        // Try to fetch from root first, then fallback to relative if needed
        var candidateUrls = [
            '/components/footer.html',
            'components/footer.html',
            '../components/footer.html',
            '../../components/footer.html'
        ];

        var loaded = false;

        for (var i = 0; i < candidateUrls.length; i++) {
            try {
                var res = await fetch(candidateUrls[i]);
                if (res.ok) {
                    var html = await res.text();
                    target.innerHTML = html;
                    updateYear(target);
                    loaded = true;
                    break;
                }
            } catch (e) {
                // Try next path
            }
        }

        if (!loaded) {
            updateYear(target);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadFooter);
    } else {
        loadFooter();
    }
})();
