import unittest
import json

from project.tests.base import BaseTestCase


class TestCoreService(BaseTestCase):

    def test_core(self):
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])

    def test_core_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Levantado</h1>', response.data)
        self.assertNotIn(b'Not Found', response.data)


if __name__ == "__main__":
    unittest.main()
