from django.test import TestCase
from django.shortcuts import resolve_url as r


class CourseDetailsTestCase(TestCase):
    fixtures = ['courses.json']

    def setUp(self):
        self.response = self.client.get(
            r('courses:details', 'curso-de-python'))

    def test_url(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'courses/details.html')

    def test_contents(self):
        contents = ['Curso de Python']

        with self.subTest():
            for c in contents:
                self.assertContains(self.response, c)
