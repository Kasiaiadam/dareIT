import time
from lib2to3.pgen2 import driver
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class Dashboard(BasePage):
    futbol_kolektyw_button_xpath = '//*[@title="Logo PANEL SKAUTINGOWY"]'
    main_page_button = "//*[text()='Main page']"
    dev_team_contact = "//a[contains(@href, 'client')]"
    # add_player_xpath = "//*div[2]/div/div/a/button"
    sign_out_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    choose_language_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    players_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
    go_to_last_created_player = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]"
    go_to_last_updated_player = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]"
    go_to_last_created_match = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]"
    go_to_last_updated_report = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts.futbolkolektyw.pl/en'
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"
    download_csv_xpath = "//*[@aria-label='Download CSV']"
    wait = WebDriverWait(driver, 10)
    expected_player_name = 'MARIAN DROZD'
    check_last_player_name_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]'
    text_players_xpath='//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span'

    def find_element(XPATH, text_players_xpath):
        pass

    def title_of_page(self):
        self.wait_for_the_element_to_be_clickable(self.futbol_kolektyw_button_xpath)
        assert self.get_page_title() == self.expected_title

    def click_on_the_add_player(self):
        self.click_on_the_element(self.add_player_xpath)

    def click_on_the_signout_button(self):
        self.click_on_the_element(self.sign_out_xpath)

    def click_on_the_change_language_button(self):
        self.click_on_the_element(self.choose_language_xpath)

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_xpath)

    def last_added_player(self):
        self.wait_for_the_element_to_be_clickable(self.futbol_kolektyw_button_xpath)
        assert self.check_last_player_name_xpath == self.expected_player_name
