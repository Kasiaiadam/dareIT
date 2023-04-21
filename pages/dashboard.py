import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):

    futbol_kolektyw_button_xpath = '//*[@title="Logo Scouts Panel"]'
    main_page_button = "//*[text()='Main page']"
    dev_team_contact = "//a[contains(@href, 'client')]"
    add_player_xpath = "//*div[2]/div/div/a/button"
    sign_out = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    choose_language = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    players = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
    go_to_last_created_player = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]"
    go_to_last_updated_player = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]"
    go_to_last_created_match = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]"
    go_to_last_updated_report = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    #add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_the_element(self.futbol_kolektyw_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player(self):
        self.click_on_the_element(self.add_player_xpath)


