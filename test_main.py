import unittest
from main import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_get_home(self):
        # Test GET request to "/"
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'URL Shortener', response.data)

    def test_post_valid_url(self):
        # Test POST with a valid https URL
        response = self.app.post('/', data=dict(url='https://www.example.com'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generated URL:', response.data)
        self.assertIn(b'https://www.example.com', response.data)

    def test_post_invalid_url(self):
        # Test POST with an invalid (non-https) URL
        response = self.app.post('/', data=dict(url='http://insecure.com'))
        self.assertEqual(response.status_code, 200)
        # The pattern validation is done on the client side via HTML, not here,
        # so we just test it processes without error
        self.assertIn(b'Generated URL:', response.data)

if __name__ == '__main__':
    unittest.main()
