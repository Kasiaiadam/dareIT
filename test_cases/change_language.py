import os
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en")
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def change_the_language_of_the_website(self):
        change_language = LoginPage(self.driver)
        change_language.click_on_the_sign_in_button()
        change_language.click_on_the_change_language_button()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
