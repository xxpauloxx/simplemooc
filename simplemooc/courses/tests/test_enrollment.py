from django.test import TestCase
from django.shortcuts import resolve_url as r


class EnrollmentTestCase(TestCase):
    fixtures = ['courses.json']

    def setUp(self):
        self.response = self.client.get(
            r('courses:enrollment', 'curso-de-python'))

    def test_url(self):
        self.assertEqual(302, self.response.status_code)

