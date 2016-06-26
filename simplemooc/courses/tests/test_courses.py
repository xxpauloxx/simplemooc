from django.test import TestCase
from django.shortcuts import resolve_url as r


class TestCourses(TestCase):
    def setUp(self):
        self.response = self.client.get(r('courses:index'))

    def test_url(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'courses/index.html')

    def test_contents(self):
        contents = ['Listagem de Cursos do SimpleMOOC',
                    'Abaixo a lista de cursos disponíveis na plataforma']

        with self.subTest():
            for c in contents:
                self.assertContains(self.response, c)
