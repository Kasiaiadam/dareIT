from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard import Dashboard


class AddPlayer(BasePage):
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"
    fill_in_email="//*[@name='email']"
    fill_in_name="//*[@name='name']"
    choose_leg="//*[ @ id = 'mui-component-select-leg']"
    submit_button="//*[@type='submit']"
    clear_button="//*[contains(@class, 'MuiButton-containedSecondary')]"
    add_link_to_youtube="//*[@aria-label='Add link to Youtube']"
    fill_in_weight="(//*[@type='number'])[1]"
    fill_in_height ="(//*[@type='number'])[2]"
    main_position="//*[@name='mainPosition']"
    choose_district="//*[contains(@id,'select-district')]"
    add_player_url='https://scouts-test.futbolkolektyw.pl/en/players/add'
    expected_title='Add player'

    # def __init__(self, driver: WebDriver):
    # super().__init__(driver)
    # self.add_player_xpath = None

    def click_on_the_add_player(self):
        self.click_on_the_element(self.add_player_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title

pass
