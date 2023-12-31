"""
Module to test the functionality of the CTS Backend.
"""

import unittest
from main import create_app

class TestCTSBackend(unittest.TestCase):
    """Test case for CTS Backend."""

    def setUp(self):
        """Set up the test case."""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_ping_endpoint(self):
        """Test the '/ping' endpoint."""
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], '200 OK')

if __name__ == '__main__':
    unittest.main()
