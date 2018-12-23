import unittest
import json

from project.tests.base import BaseTestCase


class TestCoreService(BaseTestCase):

    def test_core(self):
        response = self.client.get('/api/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])
