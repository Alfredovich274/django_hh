from django.test import TestCase, Client
from mixer.backend.django import mixer
from .models import UserHh, Profile


# Create tests
class TestUserProfile(TestCase):

    def setUp(self):
        self.user = mixer.blend(UserHh)

    def test_save(self):
        # print(Profile.objects.all())
        self.assertTrue(Profile.objects.all())
        self.assertTrue(Profile.objects.filter(id='1'))

    def test_request_api(self):
        response = self.client.get('http://127.0.0.1:8000/api/v0/cities/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('http://127.0.0.1:8000/api/v0/skills/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('http://127.0.0.1:8000/api/v0/params/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('http://127.0.0.1:8000/api/v0/experience/')
        self.assertEqual(response.status_code, 403)

        UserHh.objects.create_user(username='test_user', email='test@test.com',
                                   password='test1234')
        self.client.login(username='test_user', password='test1234')
        response = self.client.get('http://127.0.0.1:8000/api/v0/experience/')
        self.assertEqual(response.status_code, 200)
