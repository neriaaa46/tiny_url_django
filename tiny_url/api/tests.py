from django.test import TestCase
from api.models import TinyUrl


class ApiTest(TestCase):

    def setUp(self):
        TinyUrl.objects.create(id="123", url="http://google.com", counter=0)

    # Check use tiny url redirect to original url
    def test_redirect(self):
        response = self.client.get('/s/123')
        self.assertEqual(302, response.status_code)
        self.assertEqual("http://google.com", response.url)

    # Check use tiny url NOT EXIST return not found
    def test_tiny_url_not_found(self):
        response = self.client.get('/s/NOT_EXIST')
        self.assertEqual(404, response.status_code)

    # Check create tiny url - empty_body
    def test_create_tiny_url_empty_body(self):
        response = self.client.post('/create', {}, content_type="application/json")
        self.assertEqual(400, response.status_code)

    # Check create tiny url - Invalid url
    def test_create_invalid_tiny_url(self):
        response = self.client.post('/create', {"url": "123"}, content_type="application/json")
        self.assertEqual(400, response.status_code)

        response = self.client.post('/create', {"url": "htt://google.com"}, content_type="application/json")
        self.assertEqual(400, response.status_code)

        response = self.client.post('/create', {"url": "http://google."}, content_type="application/json")
        self.assertEqual(400, response.status_code)

    # Check create tiny url - correct response and tiny url Found in DB
    def test_create_tiny_url(self):
        response = self.client.post('/create', {"url": "http://amazon.com"}, content_type="application/json")
        self.assertEqual(200, response.status_code)
        url = response.content.decode("UTF-8")
        tiny_id = self.extract_id_from_url(url)
        tiny_url = TinyUrl.objects.get(id=tiny_id)
        self.assertEqual("http://amazon.com", tiny_url.url)

    def extract_id_from_url(self, url):
        return url.rpartition('/')[-1]
