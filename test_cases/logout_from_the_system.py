import os
import time
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLogoutPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        # self.driver_service=Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        # self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_logout_from_the_system(self):
        TestLoginPage.test_login_to_the_system(self)
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_signout_button()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
