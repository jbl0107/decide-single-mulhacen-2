from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from base import mods


class AuthTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        mods.mock_query(self.client)
        u = User(username='voter1')
        u.set_password('123')
        u.save()

        u2 = User(username='admin')
        u2.set_password('admin')
        u2.is_superuser = True
        u2.save()

    def tearDown(self):
        self.client = None

    def test_login(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)

        token = response.json()
        self.assertTrue(token.get('token'))

    def test_login_fail(self):
        data = {'username': 'voter1', 'password': '321'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_getuser(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 200)

        user = response.json()
        self.assertEqual(user['id'], 1)
        self.assertEqual(user['username'], 'voter1')

    def test_getuser_invented_token(self):
        token = {'token': 'invented'}
        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 404)

    def test_getuser_invalid_token(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.filter(user__username='voter1').count(), 1)

        token = response.json()
        self.assertTrue(token.get('token'))

        response = self.client.get('/authentication/logout/?next=/admin/')
        self.assertRedirects(response, '/admin/', status_code=302, target_status_code=302, fetch_redirect_response=True)

        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        # data = {'username': 'voter1', 'password': '123'}
        # response = self.client.post('/authentication/login/', data, format='json')
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(Token.objects.filter(user__username='voter1').count(), 1)

        # token = response.json()
        # self.assertTrue(token.get('token'))

        # response = self.client.post('/authentication/logout/', token, format='json')
        # self.assertEqual(response.status_code, 200)

        # self.assertEqual(Token.objects.filter(user__username='voter1').count(), 0)
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/authentication/logout/?next=/admin/')
        self.assertRedirects(response, '/admin/', status_code=302, target_status_code=302, fetch_redirect_response=True)

    def test_register_user_already_exist(self):
        data = {'username': 'admin', 'password1': 'admin', 'password2': 'admin'}
        response = self.client.post('/authentication/register/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register(self):
        data = {'username': 'Vill-V', 'password1': 'Helix5@%&', 'password2': 'Helix5@%&'}
        response = self.client.post('/authentication/register/?next=/admin/', data=data)
        self.assertRedirects(response, '/admin/', status_code=302, target_status_code=302, fetch_redirect_response=True)
