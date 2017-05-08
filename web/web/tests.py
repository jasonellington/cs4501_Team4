from django.test import TestCase
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
        resp = driver.get("http://load_balancer:8005/register")
        print(driver.title)
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
