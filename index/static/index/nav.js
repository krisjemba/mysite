document.addEventListener('DOMContentLoaded', function() {
    // Highlight current page in navigation
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;
        if (currentPath === linkPath) {
            link.classList.add('active');
        }
    });
});