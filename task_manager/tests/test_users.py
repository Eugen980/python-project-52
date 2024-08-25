from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth import get_user_model


class CRUDTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_create(self):
        username = 'Username'
        first_name = 'First_name'
        last_name = 'Last_name'
        password = 'SuperPas$$word'

        response = self.client.post(
            reverse('create_user'),
            data={'username': username,
                  'first_name': first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        self.assertRedirects(response, reverse('login'), 302)

        new_user = get_user_model().objects.get(username=username)

        self.assertEqual(new_user.username, username)
        self.assertEqual(new_user.first_name, first_name)
        self.assertEqual(new_user.last_name, last_name)

    def test_user_read(self):
        username = 'Username'
        first_name = 'First_name'
        last_name = 'Last_name'
        password = 'SuperPas$$word'

        response = self.client.post(
            reverse('create_user'),
            data={'username': username,
                  'first_name': first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        self.assertRedirects(response, reverse('login'), 302)

        new_user = get_user_model().objects.get(username=username)
        all_users = get_user_model().objects.all()

        self.assertIn(new_user, all_users)

    def test_user_update(self):

        username = 'ChackChack'
        first_name = 'Oleg'
        last_name = 'Ivanov'
        password = 'OlegOleg228'

        self.client.post(
            reverse('create_user'),
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

        user = get_user_model().objects.get(username=username)

        changed_first_name = 'Ivan'
        response = self.client.post(
            reverse('update_user', kwargs={'pk': user.pk}),
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
        username = 'SuperUser'
        first_name = 'Bart'
        last_name = 'Simpson'
        password = 'Superpa$$word'

        self.client.post(
            reverse('create_user'),
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

        user = get_user_model().objects.get(username=username)

        response = self.client.post(
            reverse('delete_user', kwargs={'pk': user.pk})
        )

        self.assertRedirects(response, reverse('users'), 302)

        deleted_user = get_user_model().objects.filter(id=user.pk)
        self.assertNotIn(user.pk, deleted_user)
