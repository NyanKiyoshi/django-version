from django.test import TestCase, Client


class MyTestCase(TestCase):
    def test_response_header(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 404)
        self.assertIn("X-Project-Version", response)
        self.assertEqual(response["X-Project-Version"], "a.b.c")
