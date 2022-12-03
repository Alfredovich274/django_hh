from django.test import TestCase, Client
from mixer.backend.django import mixer
from .models import Param, Vacancy
from userapp.models import UserHh
from faker import Faker


class TestParam(TestCase):

    def setUp(self):
        self.param = mixer.blend(Param, key_words='python')

    def test_str(self):
        self.assertEqual(str(self.param), 'python')


class TestVacancy(TestCase):

    def setUp(self):
        self.vacancy = mixer.blend(Vacancy, name='java')

    def test_str(self):
        self.assertEqual(str(self.vacancy), 'java')


class TestParamListView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        # self.fake = Faker()

    def test_views(self):
        UserHh.objects.create_user(username='test_user', email='test@test.com',
                                   password='test1234')
        response = self.client.get('/results/')
        self.assertEqual(response.status_code, 404)

        user = self.client.login(username='test_user', password='test1234')
        print('мы вошли? :',
              self.client.login(username='test_user', password='test1234'))

        response = self.client.get('/results/')  # results
        self.assertEqual(response.status_code, 300)

        # response = self.client.get('/create-options/')
        # self.assertEqual(response.status_code, 200)
#
#
# def test_contact():
#     pass
# response = self.client.post('/contact/',
#                                     {'name': self.fake.name(),
#                                      'message': self.fake.text(),
#                                      'email': self.fake.email()})
#
#
# def test_create_params():
#     pass
