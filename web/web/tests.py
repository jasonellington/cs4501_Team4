from django.test import TestCase
from selenium import webdriver
import random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumTests(TestCase):

    def setUp(self):
        self.selenium = webdriver.Remote(
            command_executor='http://selenium_chrome:4444/wd/hub/',
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def test_register_user(self):
        selenium = self.selenium
        selenium.get("http://172.17.0.10:8000/register")
        username = selenium.find_element_by_id('id_user_id')
        username.send_keys(random.randint(1, 1000000))
        password = selenium.find_element_by_id("id_password")
        password.send_keys("gohoos")
        fname = selenium.find_element_by_id("id_first_name")
        fname.send_keys("Jessica")
        lname = selenium.find_element_by_id("id_last_name")
        lname.send_keys("Zimmerman")
        age = selenium.find_element_by_id("id_age")
        age.send_keys("22")
        selenium.find_element_by_id("submit").click()
        assert "Thanks for registering!" in selenium.page_source

    def test_sign_in_and_create_listing(self):
        selenium = self.selenium
        selenium.get("http://172.17.0.10:8000/login")
        username = selenium.find_element_by_id('id_user_id')
        username.send_keys("testuser")
        password = selenium.find_element_by_id("id_password")
        password.send_keys("gohoos")
        selenium.find_element_by_id("submit").click()
        assert "User Portal" in selenium.page_source
        selenium.get("http://172.17.0.10:8000/create_listing")
        make = selenium.find_element_by_id('id_make')
        make.send_keys("Ford")
        model = selenium.find_element_by_id("id_model")
        model.send_keys("Mustang")
        year = selenium.find_element_by_id("id_year")
        year.send_keys("1967")
        color = selenium.find_element_by_id("id_color")
        color.send_keys("yellow")
        body = selenium.find_element_by_id("id_body_type")
        body.send_keys("sedan")
        seats = selenium.find_element_by_id("id_num_seats")
        seats.send_keys("4")
        selenium.find_element_by_id("submit").click()
        assert "Listing Created!" in selenium.page_source

    def test_search_functionality(self):
        selenium = self.selenium
        selenium.get("http://172.17.0.10:8000/search")
        query = selenium.find_element_by_id('id_query')
        query.send_keys("1967 Ford Mustang")
        selenium.find_element_by_id("submit").click()
        assert "Car Make: Ford" in selenium.page_source
        assert "Car Model: Mustang" in selenium.page_source
        assert "Year: 1967" in selenium.page_source

    def tearDown(self):
        self.selenium.close()
