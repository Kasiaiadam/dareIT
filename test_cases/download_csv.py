import os
import time
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.players import Players
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDownloadCSV(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_download_list_of_the_players(self):
        TestLoginPage.test_login_to_the_system(self)
        players_page = Dashboard(self.driver)
        players_page.click_on_the_players_button()
        download_list_of_the_players = Players(self.driver)
        download_list_of_the_players.click_on_the_download_csv_button()
        time.sleep(2)




    @classmethod
    def tearDown(self):
        self.driver.quit()