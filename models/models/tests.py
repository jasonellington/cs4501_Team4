from django.test import TestCase
from django.core.urlresolvers import reverse


class GetCarDetailsTestCase(TestCase):
    fixtures = ['db.json']

    #setUp method is called before each test in this class
    def setUp(self):
        pass  # nothing to set up

    def test_get_cars_success(self):
        url = reverse('get_cars')
        response = self.client.get(url).json()

        self.assertEquals(response['ok'], True)

    def test_get_car_success(self):
        url = reverse('get_car', kwargs={'car_id': 3})
        response = self.client.get(url).json()

        self.assertEquals(response['ok'], True)

    def test_get_car_fail(self):
        url = reverse('get_car', kwargs={'car_id': 0})
        response = self.client.get(url).json()

        self.assertEquals(response['ok'], False)

    def test_update_car_success(self):
        response = self.client.post('/api/v1/update/car/3/', {"make": "new"}).json()

        self.assertEquals(response['ok'], True)
        self.assertEquals(response['result']['make'], 'new')

        #tearDown method is called after each test
    def tearDown(self):
        pass  # nothing to tear down


class GetUserDetailsTestCase(TestCase):
    fixtures = ['db.json']

    #setUp method is called before each test in this class
    def setUp(self):
        pass  # nothing to set up

    def test_get_users_success(self):
        url = reverse('get_users')
        response = self.client.get(url).json()

        self.assertEquals(response['ok'], True)

    def test_get_user_success(self):
        url = reverse('get_user', kwargs={'user_id': 'abp5fn'})
        response = self.client.get(url).json()

        self.assertEquals(response['ok'], True)

    def test_get_user_fail(self):
        url = reverse('get_user', kwargs={'user_id': 'none'})
        response = self.client.get(url).json()

        self.assertEquals(response['ok'], False)

    def test_update_user_success(self):
        response = self.client.post('/api/v1/update/user/abp5fn/', {"first_name": "JAYZ"}).json()

        self.assertEquals(response['ok'], True)
        self.assertEquals(response['result']['first_name'], 'JAYZ')

    #tearDown method is called after each test
    def tearDown(self):
        pass  # nothing to tear down
