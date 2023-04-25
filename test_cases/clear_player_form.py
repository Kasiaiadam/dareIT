import os
import unittest
from selenium import webdriver
import time
from test_cases.fill_in_player_form import TestFillForm
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.add_a_player import AddPlayer


class TestClearForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_clear_player_form(self):
        TestFillForm.test_fill_in_player_form(self)
        clear = AddPlayer(self.driver)
        clear.clear_form()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
