from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from myapp.models import Car, User

class GetCarDetailsTestCase(TestCase):
	fixtures = ['db.json']

    #setUp method is called before each test in this class
	def setUp(self):
		pass #nothing to set up

	def test_get_cars_success(self):
		url = reverse('myapp:get_cars')
		response = self.client.get(url).json()

		self.assertEquals(response['ok'], True)

	def test_get_car_success(self):
		url = reverse('myapp:get_car', kwargs={'car_id':3})
		response = self.client.get(url).json()

		self.assertEquals(response['ok'], True)

	def test_get_car_fail(self):
		url = reverse('myapp:get_car', kwargs={'car_id':0})
		response = self.client.get(url).json()

		self.assertEquals(response['ok'], False)

    #tearDown method is called after each test
	def tearDown(self):
		pass #nothing to tear down
