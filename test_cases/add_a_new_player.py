import os
import time
import unittest
from selenium import webdriver
# from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
# from login_to_the_system import TestLoginPage
from pages.add_a_player import AddPlayer


class TestAddPlayer(unittest.TestCase):

    @classmethod

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        user_login = LoginPage(self.driver)
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(2)

    def test_add_a_new_player(self):
        add_player = AddPlayer(self.driver)
        add_player.click_on_the_add_player()
        add_player.title_of_page()
        time.sleep(2)


    @classmethod
    def tearDown(self):
        self.driver.quit()
