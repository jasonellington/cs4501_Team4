from django.test import TestCase
from django.core.urlresolvers import reverse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumTests(TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://selenium_chrome:4444/wd/hub/',
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def test_register_user(self):
        driver = self.driver
        resp = driver.get("http://localhost:8005/register")
        print(resp)
        username = driver.find_element_by_id("id_user_id")
        username.send_keys("jkz3km")
        password = driver.find_element_by_id("id_password")
        password.send_keys("gohoos")
        fname = driver.find_element_by_id("id_first_name")
        fname.send_keys("Jessica")
        lname = driver.find_element_by_id("id_last_name")
        lname.send_keys("Zimmerman")
        age = driver.find_element_by_id("id_age")
        age.send_keys("22")
        driver.find_element_by_id("submit").click()
        assert "Thanks for registering!" in driver.page_source

    def tearDown(self):
        self.driver.close()


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
