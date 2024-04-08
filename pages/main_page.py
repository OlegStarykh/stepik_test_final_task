from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
    def go_to_login_page(self, timeout=10):
        login_link = self.driver.find_element('xpath', '//*[@id="login_link"]')
        login_link.click()


    def should_be_login_link(self):
        wait = WebDriverWait(self.driver, 20, 1)
        login_link = ('xpath', '//*[@id="login_link"]')
        assert self.is_element_present(*login_link), "Login link is not presented"



