import os
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en")
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        super(TestLoginPage, self).setUp(self)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.title_of_page()
        user_login.title_of_box()
        user_login.click_on_the_sign_in_button()
        time.sleep(2)

    # def test_title_of_dashboard_page(self):
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()


