from django.test import TestCase, Client
from django.urls import reverse

from task_manager.users.models import User


class CRUDTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_create(self):
        username = 'Username'
        first_name = 'First_name'
        last_name = 'Last_name'
        password = 'SuperPas$$word'

        response = self.client.post(
            reverse('user_create'),
            data={'username': username,
                  'first_name': first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        self.assertRedirects(response, reverse('login'), 302)

        new_user = User.objects.get(username=username)

        self.assertEqual(new_user.username, username)
        self.assertEqual(new_user.first_name, first_name)
        self.assertEqual(new_user.last_name, last_name)

    def test_user_read(self):
        username = 'Username'
        first_name = 'First_name'
        last_name = 'Last_name'
        password = 'SuperPas$$word'

        response = self.client.post(
            reverse('user_create'),
            data={'username': username,
                  'first_name': first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        self.assertRedirects(response, reverse('login'), 302)

        new_user = User.objects.get(username=username)
        all_users = User.objects.all()

        self.assertIn(new_user, all_users)

    def test_user_update(self):

        username = 'ChackChack'
        first_name = 'Oleg'
        last_name = 'Ivanov'
        password = 'OlegOleg228'

        self.client.post(
            reverse('user_create'),
            data={'username': username,
                  'first_name': first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        self.client.post(
            reverse('login'),
            data={'username': username,
                  'password': password}
        )

        user = User.objects.get(username=username)

        changed_first_name = 'Ivan'
        response = self.client.post(
            reverse('user_update', kwargs={'pk': user.pk}),
            data={'username': username,
                  'first_name': changed_first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        self.assertRedirects(response, reverse('users'))

        user.refresh_from_db()
        self.assertEqual(user.first_name, changed_first_name)

    def test_user_delete(self):
        username = 'Batman'
        first_name = 'Bruce'
        last_name = 'Wayne'
        password = 'Superman'

        self.client.post(
            reverse('user_create'),
            data={'first_name': first_name,
                  'last_name': last_name,
                  'username': username,
                  'password1': password,
                  'password2': password}
        )

        self.client.post(
            reverse('login'),
            data={'username': username,
                  'password': password}
        )

        user = User.objects.get(username=username)

        response = self.client.post(
            reverse('user_delete', kwargs={'pk': user.pk})
        )

        self.assertRedirects(response, reverse('users'), 302)

        deleted_user = User.objects.filter(id=user.pk)
        self.assertNotIn(user.pk, deleted_user)
