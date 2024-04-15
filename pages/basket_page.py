from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .lokators import BasePageLocators
from .lokators import BasketPageLocators


class BasketPage(BasePage):
    def basket_page_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.TOTAL_BASKET_PRICE), "The basket is not empty"

    def basket_page_is_empty_current_message(self):
        assert self.is_element_present('xpath', '//*[@id="content_inner"]/p'), 'no empty basket message'
