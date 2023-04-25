from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@name='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    expected_title = "Scouts panel - sign in"
    change_language_button_xpath = "//*[@value='en']"
    title_of_box_xpath = "//*[contains(@class, 'MuiTypography-h5')]"
    header_of_box = 'Scouts Panel'

    def title_of_box(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title() == self.expected_title

    def click_on_the_change_language_button(self):
        self.click_on_the_element(self.change_language_button_xpath)
