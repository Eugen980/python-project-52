from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.statuses.models import Status


class CRUDTest(TestCase):
    model = get_user_model()

    def setUp(self):
        self.client = Client()
        self.user = self.model.objects.create_user(username='Test',
                                                   password='password')

    def test_create_status(self):
        name = 'In dev'

        self.client.force_login(self.user)

        response = self.client.post(reverse('status_create'),
                                    data={'name': name})

        self.assertRedirects(response, reverse('statuses'))

        new_status = Status.objects.get(name=name)
        all_statuses = Status.objects.all()

        self.assertIn(new_status, all_statuses)

    def test_read_status(self):
        name = 'In work'

        self.client.force_login(self.user)

        response = self.client.post(reverse('status_create'),
                                    data={'name': name})

        self.assertRedirects(response, reverse('statuses'))

    def test_update_status(self):
        name = 'In dev'

        self.client.force_login(self.user)

        self.client.post(reverse('status_create'),
                         data={'name': name})

        status = Status.objects.get(name=name)

        changed_status = 'In work'

        response = self.client.post(reverse('status_update',
                                            kwargs={'pk': status.pk}),
                                    data={'name': changed_status})

        self.assertRedirects(response, reverse('statuses'))

        status.refresh_from_db()

        self.assertEqual(status.name, changed_status)

    def test_delete_status(self):
        name = 'Bad_Status'

        self.client.force_login(self.user)

        self.client.post(reverse('status_create'),
                         data={'name': name})

        status = Status.objects.get(name=name)

        response = self.client.post(reverse('status_delete',
                                            kwargs={'pk': status.pk}))

        self.assertRedirects(response, reverse('statuses'))

        deleted_status = Status.objects.filter(id=status.pk)
        self.assertNotIn(status.pk, deleted_status)
