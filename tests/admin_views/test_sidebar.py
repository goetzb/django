from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(ROOT_URLCONF='admin_views.urls')
class AdminSidebarTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(username='super', password='secret', email='super@example.com')

    def setUp(self):
        self.client.force_login(self.superuser)

    @override_settings(ADMIN_ENABLE_NAV_SIDEBAR=True)
    def test_sidebar_appears_on_index(self):
        response = self.client.get(reverse('admin:index'))
        self.assertContains(response, '<nav class="nav-sidebar">')

    @override_settings(ADMIN_ENABLE_NAV_SIDEBAR=False)
    def test_sidebar_disabled(self):
        response = self.client.get(reverse('admin:index'))
        self.assertNotContains(response, '<nav class="nav-sidebar">')

    @override_settings(ADMIN_ENABLE_NAV_SIDEBAR=True)
    def test_sidebar_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('admin:login'))
        self.assertNotContains(response, '<nav class="nav-sidebar">')
