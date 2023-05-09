import os
import unittest
from selenium import webdriver
import time

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from test_cases.fill_in_player_form import TestFillForm
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.add_a_player import AddPlayer


class TestClearForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_clear_player_form(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player()
        add_player = AddPlayer(self.driver)
        add_player.type_in_email('marian@amorki.pl')
        add_player.type_in_name('Marian')
        clear = AddPlayer(self.driver)
        clear.clear_form()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
