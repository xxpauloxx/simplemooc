from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings

from simplemooc.courses.models import Course


class ContactTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Django', slug='django')

    def tearDown(self):
        self.course.delete()

    def test_contact_form_error(self):
        data = {'name': 'Fulano de Tal', 'email': '', 'message': ''}
        client = Client()

        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)

        self.assertFormError(
            response, 'form', 'email', 'Este campo é obrigatório.')

        self.assertFormError(
            response, 'form', 'message', 'Este campo é obrigatório.')

    def test_contact_form_success(self):
        data = {
            'name': 'Fulano de Tal',
            'email': 'admin@admin.com',
            'message': 'Oi'
        }

        client = Client()
        path = reverse('courses:details', args=[self.course.slug])

        response = client.post(path, data)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])
