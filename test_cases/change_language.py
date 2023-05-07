import os
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestChangeLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_change_the_language_of_the_website(self):
        TestLoginPage.test_login_to_the_system(self)
        change_language = Dashboard(self.driver)
        time.sleep(2)
        change_language.click_on_the_change_language_button()
        time.sleep(2)
        change_language.click_on_the_change_language_button()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.driver.quit()
