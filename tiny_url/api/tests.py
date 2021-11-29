from django.test import TestCase
from api.models import TinyUrl


class ApiTest(TestCase):

    def setUp(self):
        TinyUrl.objects.create(id="123", url="http://google.com", counter=0)

    def test_redirect(self):
        response = self.client.get('/s/123')
        self.assertEqual(302, response.status_code)
        self.assertEqual("http://google.com", response.url)

    def test_tiny_url_not_found(self):
        response = self.client.get('/s/NOT_EXIST')
        self.assertEqual(404, response.status_code)

    def test_create_tiny_url_empty_body(self):
        response = self.client.post('/create', {}, content_type="application/json")
        self.assertEqual(400, response.status_code)

    # def test_create_invalid_tiny_url(self):
    #     response = self.client.post('/create', {"url": "123"}, content_type="application/json")
    #     self.assertEqual(400, response.status_code)

    def test_create_tiny_url(self):
        response = self.client.post('/create', {"url": "http://amazon.com"}, content_type="application/json")
        self.assertEqual(200, response.status_code)
        url = response.content.decode("UTF-8")
        tiny_id = self.extract_id_from_url(url)
        tiny_url = TinyUrl.objects.get(id=tiny_id)
        self.assertEqual("http://amazon.com", tiny_url.url)

    def extract_id_from_url(self, url):
        return url.rpartition('/')[-1]