/**
 * EdgeGrid Traders Capital | Core Platform Controller
 * Billion-Dollar Fintech UI/UX & Native Mobile App Experience
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Current Year Footer
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // 2. Theme Toggle Controller
    const themeToggle = document.getElementById('themeToggle');
    const html = document.documentElement;
    const savedTheme = localStorage.getItem('theme') || 'light'; // Default to light theme until changed
    html.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const currentTheme = html.getAttribute('data-theme') || 'light';
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeToggle) return;
        const icon = themeToggle.querySelector('i');
        if (icon) {
            icon.className = theme === 'light' ? 'bx bx-moon' : 'bx bx-sun';
        }
    }

    // 3. Mobile App Drawer Controls
    initMobileDrawer();

    function initMobileDrawer() {
        // Drawer toggle buttons
        const menuTriggers = document.querySelectorAll('.mobile-menu-trigger');
        const drawer = document.querySelector('.mobile-app-drawer');
        const overlay = document.querySelector('.drawer-overlay');
        const closeBtn = document.querySelector('.drawer-close');

        if (!drawer || !overlay) return;

        menuTriggers.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                openDrawer();
            });
        });

        if (closeBtn) {
            closeBtn.addEventListener('click', closeDrawer);
        }

        overlay.addEventListener('click', closeDrawer);

        function openDrawer() {
            drawer.classList.add('active');
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeDrawer() {
            drawer.classList.remove('active');
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }

        // Expose to window
        window.openMobileDrawer = openDrawer;
        window.closeMobileDrawer = closeDrawer;
    }

    // 4. Mobile Bottom Navigation Active Tab Sync
    syncBottomNav();

    function syncBottomNav() {
        const path = window.location.pathname.toLowerCase();
        const navLinks = document.querySelectorAll('.mobile-bottom-nav a');
        
        navLinks.forEach(link => {
            const href = link.getAttribute('href').toLowerCase();
            if (path.endsWith(href) || (href === 'index.html' && (path.endsWith('/') || path === ''))) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }

    // 5. Live Wall Street FX & Crypto Ticker
    initLiveTicker();

    function initLiveTicker() {
        const tickerData = [
            { symbol: "EUR/USD", price: 1.0854, change: 0.14, digits: 4, pipSize: 0.0001 },
            { symbol: "GBP/USD", price: 1.2642, change: -0.06, digits: 4, pipSize: 0.0001 },
            { symbol: "USD/JPY", price: 150.28, change: 0.38, digits: 2, pipSize: 0.01 },
            { symbol: "XAU/USD", price: 2038.20, change: 1.24, digits: 2, pipSize: 0.1 },
            { symbol: "BTC/USD", price: 64450.00, change: 2.85, digits: 2, pipSize: 1.0 },
            { symbol: "US30", price: 39120.00, change: -0.25, digits: 2, pipSize: 1.0 },
            { symbol: "NAS100", price: 18240.50, change: 0.82, digits: 2, pipSize: 1.0 }
        ];

        let tickerWrap = document.querySelector('.ticker-wrap');
        if (!tickerWrap) {
            tickerWrap = document.createElement('div');
            tickerWrap.className = 'ticker-wrap';
            const navbar = document.querySelector('.navbar');
            if (navbar) {
                navbar.insertAdjacentElement('afterend', tickerWrap);
            }
        }

        const itemsHTML = tickerData.map((item, index) => {
            const isPos = item.change >= 0;
            return `
                <div class="ticker__item" data-index="${index}">
                    <span class="ticker__symbol">${item.symbol}</span>
                    <span class="ticker__price mono-nums">${item.price.toFixed(item.digits)}</span>
                    <span class="ticker__change ${isPos ? 'positive' : 'negative'}">
                        <i class='bx ${isPos ? 'bx-up-arrow-alt' : 'bx-down-arrow-alt'}'></i> 
                        ${Math.abs(item.change).toFixed(2)}%
                    </span>
                </div>
            `;
        }).join('');

        tickerWrap.innerHTML = `<div class="ticker">${itemsHTML}${itemsHTML}${itemsHTML}</div>`;

        // Start high-velocity institutional price fluctuations
        setInterval(() => {
            const updateCount = Math.floor(Math.random() * 3) + 2;
            for (let i = 0; i < updateCount; i++) {
                const index = Math.floor(Math.random() * tickerData.length);
                const item = tickerData[index];
                const movePips = Math.floor(Math.random() * 5) - 2;
                if (movePips === 0) continue;

                const oldPrice = item.price;
                item.price += (movePips * item.pipSize);

                const priceElements = document.querySelectorAll(`.ticker__item[data-index="${index}"] .ticker__price`);
                const isUp = item.price > oldPrice;
                const flashClass = isUp ? 'price-flash-up' : 'price-flash-down';

                priceElements.forEach(el => {
                    el.textContent = item.price.toFixed(item.digits);
                    el.classList.remove('price-flash-up', 'price-flash-down');
                    void el.offsetWidth;
                    el.classList.add(flashClass);
                });
            }
        }, 500);
    }
});

// 6. Global WhatsApp Concierge Controls
window.toggleWAPopup = function() {
    const popup = document.getElementById('waPopup');
    if (!popup) return;
    popup.classList.toggle('active');
    if (popup.classList.contains('active')) {
        const input = document.getElementById('waMessageInput');
        if (input) input.focus();
    }
};

window.sendWAMessage = function() {
    const input = document.getElementById('waMessageInput');
    if (!input) return;
    const message = input.value.trim();
    if (message) {
        navigator.clipboard.writeText(message).catch(err => console.log('Clipboard:', err)).finally(() => {
            const encodedMsg = encodeURIComponent(message);
            window.open(`https://wa.me/260973493949?text=${encodedMsg}`, '_blank');
            input.value = '';
            toggleWAPopup();
        });
    }
};

// 7. Global Enrollment Modal Controls
window.openEnrollModal = function(courseName) {
    const modal = document.getElementById('enrollModal');
    if (!modal) return;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    
    // Auto-select or prefill if passed
    if (courseName) {
        const title = modal.querySelector('.enroll-modal-header h3');
        if (title) title.textContent = `Enroll in ${courseName}`;
    }
};

window.closeEnrollModal = function() {
    const modal = document.getElementById('enrollModal');
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
};

window.submitEnrollment = function() {
    const name = document.getElementById('enrolName')?.value.trim();
    const country = document.getElementById('enrolCountry')?.value.trim();
    const experience = document.getElementById('enrolExperience')?.value;
    const funds = document.getElementById('enrolFunds')?.value;

    if (!name || !country) {
        alert('Please fill in your name and country to proceed.');
        return;
    }

    const message = `*EdgeGrid Traders Application*\n\n*Name:* ${name}\n*Country:* ${country}\n*Experience:* ${experience}\n*Source of Funds:* ${funds}\n\nI would like to join the EdgeGrid Traders Capital program.`;

    navigator.clipboard.writeText(message).catch(err => console.log('Clipboard:', err)).finally(() => {
        const encodedMsg = encodeURIComponent(message);
        window.open(`https://wa.me/260973493949?text=${encodedMsg}`, '_blank');
        closeEnrollModal();
    });
};
