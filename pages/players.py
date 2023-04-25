from lib2to3.pgen2 import driver
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class Players(BasePage):
    download_csv_xpath = "//*[@aria-label='Download CSV']"
    print_button_xpath = "//*[@title='Print']"
    wait = WebDriverWait(driver, 10)

    def click_on_the_download_csv_button(self):
        self.wait_for_visibility_of_element_located(self.print_button_xpath)
        self.click_on_the_element(self.download_csv_xpath)