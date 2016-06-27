from django.test import TestCase
from django.shortcuts import resolve_url as r


class TestLogout(TestCase):
    def setUp(self):
        self.response = self.client.get(r('accounts:logout'))

    def test_url(self):
        self.assertEqual(302, self.response.status_code)
