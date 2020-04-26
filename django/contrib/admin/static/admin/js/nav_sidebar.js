{
    let main = document.getElementById('main');
    let toggleNavSidebar = document.getElementById('toggle-nav-sidebar');
    let navSidebarIsOpen = localStorage.getItem('django.admin.navSidebarIsOpen');

    if (navSidebarIsOpen === null) {
        navSidebarIsOpen = 'true';
    }
    if (navSidebarIsOpen === 'true') {
        main.classList.add('shifted');
    } else {
        main.classList.remove('shifted');
    }

    toggleNavSidebar.addEventListener('click', function() {
        'use strict';
        if (navSidebarIsOpen == 'true') {
            navSidebarIsOpen = 'false';
        } else {
            navSidebarIsOpen = 'true';
        }
        localStorage.setItem('django.admin.navSidebarIsOpen', navSidebarIsOpen);
        main.classList.toggle('shifted');
    });
}
