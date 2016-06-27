from django.test import TestCase
from django.shortcuts import resolve_url as r


class TestLogin(TestCase):
    def setUp(self):
        self.response = self.client.get(r('accounts:login'))

    def test_url(self):
        self.assertEqual(200, self.response.status_code)
