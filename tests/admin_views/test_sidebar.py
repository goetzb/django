from django.contrib import admin
from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import path, reverse


class AdminSiteWithSidebar(admin.AdminSite):
    pass


class AdminSiteWithoutSidebar(admin.AdminSite):
    enable_nav_sidebar = False


site_with_sidebar = AdminSiteWithSidebar(name="test_with_sidebar")
site_without_sidebar = AdminSiteWithoutSidebar(name="test_without_sidebar")

site_with_sidebar.register(User)

urlpatterns = [
    path('test_sidebar/admin/', site_with_sidebar.urls),
    path('test_wihout_sidebar/admin/', site_without_sidebar.urls),
]


class AdminSidebarTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(username='super', password='secret', email='super@example.com')

    def setUp(self):
        self.client.force_login(self.superuser)

    @override_settings(ROOT_URLCONF='admin_views.test_sidebar')
    def test_sidebar_appears_on_index(self):
        response = self.client.get(reverse('test_with_sidebar:index'))
        self.assertContains(response, '<nav class="nav-sidebar"')

    @override_settings(ROOT_URLCONF='admin_views.test_sidebar')
    def test_sidebar_disabled(self):
        response = self.client.get(reverse('test_without_sidebar:index'))
        self.assertNotContains(response, '<nav class="nav-sidebar"')

    @override_settings(ROOT_URLCONF='admin_views.test_sidebar')
    def test_sidebar_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('test_with_sidebar:login'))
        self.assertNotContains(response, '<nav class="nav-sidebar"')

    @override_settings(ROOT_URLCONF='admin_views.test_sidebar')
    def test_sidebar_aria_current_page(self):
        response = self.client.get(reverse('test_with_sidebar:auth_user_changelist'))
        self.assertContains(response, '<nav class="nav-sidebar"')
        self.assertContains(response, '<li class="nav-model nav-model-user" aria-current="page">')
