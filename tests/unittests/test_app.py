
import os
from application import app
import unittest
from flask import jsonify

class FlaskRouteTestCase(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True

	def tearDown(self):
		pass

	def test_home_route(self):
		with app.test_client() as client:
			resp = client.get('/')
			self.assertEqual(resp.status_code, 200)

	def test_print_url_param(self):
		with app.test_client() as client:
			url_arg = 'hello'
			result = client.get('/print/{}'.format(url_arg))
			exp_resp = jsonify(resp=url_arg).data
			self.assertEqual(result.data, exp_resp)

	def test_page_not_found(self):
		with app.test_client() as client:
			resp = client.get('/unicorn/test/view')
			self.assertEqual(resp.status_code, 404)

if __name__ == '__main__':
	unittest.main()