{
    let main = document.getElementById('main');
    let toggleNavSidebar = document.getElementById('toggle-nav-sidebar');
    let navSidebarIsOpen = localStorage.getItem('django.admin.navSidebarIsOpen');

    main.classList.toggle('shifted', navSidebarIsOpen === 'true');

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
