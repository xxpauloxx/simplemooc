from django.test import TestCase
from simplemooc.accounts.models import User
from django.shortcuts import resolve_url as r


class TestEdit(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='paulo', email='paulo.pinda@gmail.com', password='123')
        self.client.login(username='paulo', password='123')

        self.response = self.client.get(r('accounts:edit'))

    def test_url(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'accounts/edit.html')
