document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    
    if (darkModeToggle) {
        if (localStorage.getItem('dark-mode') === 'true') {
            darkModeToggle.checked = true;
        }
        
        darkModeToggle.addEventListener('change',() => {
            localStorage.setItem('dark-mode', darkModeToggle.checked);
        });
    }

    document.addEventListener('click', (event) => {
        const dropdowns = document.querySelectorAll('details.dropdown');
        
        dropdowns.forEach((dropdown) => {
            if (dropdown.hasAttribute('open') && !dropdown.contains(event.target)) {
                dropdown.removeAttribute('open'); // Tutup dropdown
            }
        });
    });
});