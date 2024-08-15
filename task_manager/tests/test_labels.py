from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.labels.models import Label


class CRUDTest(TestCase):
    model = get_user_model()

    def setUp(self):
        self.client = Client()
        self.user = self.model.objects.create_user(username='Test',
                                                   password='password')

    def test_create_label(self):
        name = 'test'

        self.client.force_login(self.user)

        response = self.client.post(reverse('label_create'),
                                    data={'name': name})

        self.assertRedirects(response, reverse('labels'))

        new_label = Label.objects.get(name=name)
        all_labels = Label.objects.all()

        self.assertIn(new_label, all_labels)

    def test_read_label(self):
        name = 'Red_flag'

        self.client.force_login(self.user)

        response = self.client.post(reverse('label_create'),
                                    data={'name': name})

        self.assertRedirects(response, reverse('labels'))

    def test_update_label(self):
        name = 'test'

        self.client.force_login(self.user)

        self.client.post(reverse('label_create'),
                         data={'name': name})

        label = Label.objects.get(name=name)

        changed_label = 'works'

        response = self.client.post(reverse('label_update',
                                            kwargs={'pk': label.pk}),
                                    data={'name': changed_label})

        self.assertRedirects(response, reverse('labels'))

        label.refresh_from_db()

        self.assertEqual(label.name, changed_label)

    def test_delete_status(self):
        name = 'Bad_label'

        self.client.force_login(self.user)

        self.client.post(reverse('label_create'),
                         data={'name': name})

        label = Label.objects.get(name=name)

        response = self.client.post(reverse('label_delete',
                                            kwargs={'pk': label.pk}))

        self.assertRedirects(response, reverse('labels'))

        deleted_label = Label.objects.filter(id=label.pk)
        self.assertNotIn(label.pk, deleted_label)
