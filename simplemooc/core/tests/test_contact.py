from django.test import TestCase
from django.shortcuts import resolve_url as r


class ContactTestCase(TestCase):
    def setUp(self):
        self.response = self.client.get(r('core:contact'))

    def test_url(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_contents(self):
        contents = ['Fale conosco', 'Links']

        with self.subTest():
            for c in contents:
                self.assertContains(self.response, c)
