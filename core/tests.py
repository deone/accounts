from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class ViewsTests(TestCase):

    def setup(self):
        self.c = Client()

class CreateTests(ViewsTests):

    def test_create(self):
        response = self.c.get(reverse('accounts:create'))

        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(json.loads(response.content)['status'], 'ok')