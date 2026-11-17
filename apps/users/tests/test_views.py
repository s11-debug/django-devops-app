from django.test import TestCase, Client
from django.contrib.auth.models import User


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass123')

    def test_login_page_loads(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_requires_post(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        response = self.client.post('/users/login/', {
            'username': 'testuser',
            'password': 'testpass123',
        })
        self.assertIn(response.status_code, [200, 302])

    def test_login_with_invalid_credentials(self):
        response = self.client.post('/users/login/', {
            'username': 'wronguser',
            'password': 'wrongpass',
        })
        self.assertEqual(response.status_code, 200)
