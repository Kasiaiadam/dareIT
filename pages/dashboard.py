<<<<<<< HEAD
import time

=======
>>>>>>> 7441633d8ff2969b3f958cecc9bc07ef0f107aff
from pages.base_page import BasePage


class Dashboard(BasePage):
<<<<<<< HEAD
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


pass


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
=======
    main_page_button="//*[text()='Main page']"
    dev_team_contact="//a[contains(@href, 'client')]"
    add_player_hyperlink= "//a[contains(@href, 'add')]"
    sign_out="//ul[2]/div[2]"
    choose_language="//ul[2]/div[1]"
    players="//ul[1]/div[2]"
    go_to_last_created_player="//div[3]/div/div/a[1]"
    go_to_last_updated_player ="//div/a[2]"
    go_to_last_created_match ="//div/a[3]"
    go_to_last_updated_report="//div/a[5]]"
pass
>>>>>>> 7441633d8ff2969b3f958cecc9bc07ef0f107aff