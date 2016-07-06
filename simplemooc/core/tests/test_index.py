from django.test import TestCase
from django.shortcuts import resolve_url as r


class IndexTestCase(TestCase):
    def setUp(self):
        self.response = self.client.get(r('core:home'))

    def test_url(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_contents(self):
        contents = ['Início',
                    'Cursos',
                    'Contato',
                    'Publique suas aulas',
                    'Interaja com seus Alunos',
                    'Envie anúncios diretamente para os alunos',
                    'Crie exercícios para avaliar seus alunos']

        with self.subTest():
            for c in contents:
                self.assertContains(self.response, c)
