from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.valid_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'phone': '9876543210',
            'password': 'Test@1234',
            'confirm_password': 'Test@1234'
        }
        User.objects.create_user(
            username='existing@example.com',
            email='existing@example.com',
            password='password123'
        )

    def test_successful_registration(self):
        response = self.client.post(
            self.register_url,
            data=self.valid_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

    def test_missing_first_name(self):
        data = self.valid_data.copy()
        data.pop('first_name')
        response = self.client.post(
            self.register_url,
            data=data
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('First name is required', str(response.content))

    def test_weak_password(self):
        data = self.valid_data.copy()
        data['password'] = data['confirm_password'] = 'weak'
        response = self.client.post(
            self.register_url,
            data=data
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password must be at least 8 characters', str(response.content))

    def test_password_mismatch(self):
        data = self.valid_data.copy()
        data['confirm_password'] = 'Different@123'
        response = self.client.post(
            self.register_url,
            data=data
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('Passwords do not match', str(response.content))

    def test_duplicate_email(self):
        data = self.valid_data.copy()
        data['email'] = 'existing@example.com'
        response = self.client.post(
            self.register_url,
            data=data
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email already registered', str(response.content))
