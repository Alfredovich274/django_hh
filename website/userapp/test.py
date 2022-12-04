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
