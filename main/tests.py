from django.test import TestCase

# Create your tests here.
class MainTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')