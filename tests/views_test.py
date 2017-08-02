import unittest
import sys
import os
from flask import jsonify
sys.path.append(os.path.join(os.getcwd(), '..'))


from ipy import app


class ViewsTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_ip(self):
        """GET /
        """
        self.result = self.app.get('/')
        self.result = self.result.data.decode()
        self.assertEqual(self.result, '127.0.0.1')

    def test_get_ip_json(self):
        """GET /?format=json
        """
        with app.test_request_context():
            self.result = self.app.get('/?output=json')
            self.result = self.result.data.decode()
            self.expected = jsonify(ip='127.0.0.1').data.decode()
            self.assertEqual(self.result, self.expected)


if __name__ == '__main__':
    unittest.main()
