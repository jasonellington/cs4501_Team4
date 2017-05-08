from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumTests(TestCase):

    def setUp(self):
        self.selenium = webdriver.Remote(
            command_executor='http://selenium_chrome:4444/wd/hub/',
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def test_register_user(self):
        selenium = self.selenium
        resp = selenium.get("http://172.17.0.10:8000/register")
        username = selenium.find_element_by_id('id_user_id')
        username.send_keys("jkz3km")
        password = selenium.find_element_by_id("id_password")
        password.send_keys("gohoos")
        fname = selenium.find_element_by_id("id_first_name")
        fname.send_keys("Jessica")
        lname = selenium.find_element_by_id("id_last_name")
        lname.send_keys("Zimmerman")
        age = selenium.find_element_by_id("id_age")
        age.send_keys("22")
        selenium.find_element_by_id("submit").click()
        assert "http://172.17.0.10:8000/register" in selenium.current_url

    def tearDown(self):
        self.selenium.close()
