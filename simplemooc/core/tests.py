from django.test import TestCase


class TestIndex(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_url(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
