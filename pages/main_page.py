from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .lokators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self, timeout=10):
        self.driver.find_element(*MainPageLocators.LOGIN_LINK).click()


    def should_be_login_link(self):
        wait = WebDriverWait(self.driver, 20, 1)
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented on main page"



