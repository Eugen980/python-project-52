from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.tasks.models import Task


class CRUDTest(TestCase):
    model = get_user_model()

    def setUp(self):
        self.client = Client()
        self.user = self.model.objects.create_user(username='Test',
                                                   password='password')

    def test_create_task(self):
        name = 'Sleep'
        status = 'In work'

        self.client.force_login(self.user)

        status_created = self.client.post(reverse('status_create'),
                                          data={'name': status})

        response = self.client.post(reverse('task_create'),
                                    data={'name': name,
                                          'status': status_created})

        self.assertRedirects(response, reverse('tasks'), 302)

        new_task = Task.objects.get(name=name)
        all_tasks = Task.objects.all()

        self.assertIn(new_task, all_tasks)

    def show_task_for_auth_user(self):
        name = 'Watch TV'
        status = 'Extra status'

        username = 'Batman'
        first_name = 'Bruce'
        last_name = 'Wayne'
        password = 'Superman'

        response = self.client.post(
            reverse('user_create'),
            data={'username': username,
                  'first_name': first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        self.assertRedirects(response, reverse('login'), 302)

        status_created = self.client.post(reverse('status_create'),
                                          data={'name': status})

        response = self.client.post(reverse('task_create'),
                                    data={'name': username,
                                          'status': status_created})

        self.assertRedirects(response, reverse('tasks'), 302)

        new_task = Task.objects.get(name=name)
        all_tasks = Task.objects.all()

        self.assertIn(new_task, all_tasks)

    def test_read_task(self):
        name = 'Sleep'
        status = 'In work'

        self.client.force_login(self.user)

        status_created = self.client.post(reverse('status_create'),
                                          data={'name': status})

        response = self.client.post(reverse('task_create'),
                                    data={'name': name,
                                          'status': status_created})

        self.assertRedirects(response, reverse('tasks'), 302)

    def test_update_task(self):
        name = 'Sleep'
        status = 'In work'

        self.client.force_login(self.user)

        status_created = self.client.post(reverse('status_create'),
                                          data={'name': status})

        response = self.client.post(reverse('task_create'),
                                    data={'name': name,
                                          'status': status_created})

        self.assertRedirects(response, reverse('tasks'), 302)

        task = Task.objects.get(name=name)

        changed_task = 'Watch TV'

        response = self.client.post(reverse('task_update',
                                            kwargs={'pk': task.pk}),
                                    data={'name': changed_task})

        self.assertRedirects(response, reverse('tasks'))

        task.refresh_from_db()

        self.assertEqual(task.name, changed_task)

    def test_delete_task(self):
        name = 'Flying in a dream'
        status = 'In work'

        self.client.force_login(self.user)

        status_created = self.client.post(reverse('status_create'),
                                          data={'name': status})

        response = self.client.post(reverse('task_create'),
                                    data={'name': name,
                                          'status': status_created})

        self.assertRedirects(response, reverse('tasks'), 302)
        task = Task.objects.get(name=name)

        response = self.client.post(reverse('task_delete',
                                            kwargs={'pk': task.pk}))

        self.assertRedirects(response, reverse('tasks'))

        deleted_task = Task.objects.filter(id=task.pk).exists()
        self.assertFalse(deleted_task)
