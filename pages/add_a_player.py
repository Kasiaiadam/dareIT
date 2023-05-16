from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard import Dashboard


class AddPlayer(BasePage):
    fill_in_email_xpath = "//*[@name='email']"
    fill_in_name_xpath = "//*[@name='name']"
    choose_leg_xpath = "//*[@id = 'mui-component-select-leg']"
    submit_button_xpath = "//*[@type='submit']"
    clear_button_xpath = "//*[contains(@class, 'MuiButton-containedSecondary')]"
    add_link_to_youtube_xpath = "//*[@aria-label='Add link to Youtube']"
    fill_in_youtube_link_xpath = "//*[@name='webYT[0]']"
    fill_in_weight_xpath = "(//*[@type='number'])[1]"
    fill_in_height_xpath = "(//*[@type='number'])[2]"
    main_position_xpath = "//*[@name='mainPosition']"
    choose_district_xpath = "//*[@id='mui-component-select-district']"
    district_xpath = "//*[@data-value='lubelskie']"
    add_player_url = 'https://scouts.futbolkolektyw.pl/en/players/add'
    expected_title = 'Add player'
    fill_in_club_xpath = "//*[@name='club']"
    fill_in_second_position_xpath = "//*[@name='secondPosition']"
    fill_in_achievements_xpath = "//*[@name='achievements']"
    choose_age_xpath = "//*[@name='age']"
    fill_in_level_xpath = "//*[@name='level']"
    fill_in_phone_xpath = "//*[@name='phone']"
    fill_in_surname_xpath = "//*[@name='surname']"
    add_language_button_xpath = "//*[@aria-label='Add language']"
    fill_in_language_xpath = "//*[@name='languages[0]']"
    left_leg_xpath = "//*[@data-value='left']"
    right_leg_xpath = "//*[@data-value='right']"  # spróbuj inaczej !!!
    main_page_button_xpath = "//ul[1]/div[1]"
    success_container_xpath = "//*[@id='__next']/div[2]/div"
    previous_club_xpath = "//*[@name='exClub']"

    # def __init__(self, driver: WebDriver):
    # super().__init__(driver)
    # self.add_player_xpath = None
    def click_on_the_main_page(self):
        #self.wait_for_visibility_of_element_located(self.success_container_xpath)
        self.click_on_the_element(self.main_page_button_xpath)

    def click_on_the_choose_district(self):
        self.click_on_the_element(self.choose_district_xpath)

    def choose_district(self):
        self.click_on_the_element(self.district_xpath)

    def clear_form(self):
        self.click_on_the_element(self.clear_button_xpath)

    def title_of_page(self):
        assert self.get_page_title() == self.expected_title

    def type_in_age(self, age):
        self.field_send_keys(self.choose_age_xpath, age)

    def type_in_exclub(self, previousclub):
        self.field_send_keys(self.previous_club_xpath, previousclub)

    def type_in_email(self, email):
        self.field_send_keys(self.fill_in_email_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.fill_in_name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.fill_in_surname_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.fill_in_phone_xpath, phone)

    def click_on_the_choose_leg_button(self):
        self.click_on_the_element(self.choose_leg_xpath)

    def type_in_weight(self, weight):
        self.field_send_keys(self.fill_in_weight_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.fill_in_height_xpath, height)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_xpath, position)

    def click_add_link_to_youtube(self):
        self.click_on_the_element(self.add_link_to_youtube_xpath)

    def type_in_youtube_link(self, youtube_link):
        self.field_send_keys(self.fill_in_youtube_link_xpath, youtube_link)

    def type_in_main_club(self, club):
        self.field_send_keys(self.fill_in_club_xpath, club)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.fill_in_achievements_xpath, achievements)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.fill_in_second_position_xpath, second_position)

    def type_in_level(self, level):
        self.field_send_keys(self.fill_in_level_xpath, level)

    def click_on_the_language_button(self):
        self.click_on_the_element(self.add_language_button_xpath)

    def type_in_language(self, language):
        self.field_send_keys(self.fill_in_language_xpath, language)

    def click_on_the_right_leg(self):
        self.click_on_the_element(self.right_leg_xpath)

    def click_on_the_submit(self):
        self.click_on_the_element(self.submit_button_xpath)


pass
