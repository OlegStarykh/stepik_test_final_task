from .base_page import BasePage
from .lokators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.is_element_present(
            *ProductPageLocators.ADD_TO_CART_BUTTON), "ADD_TO_CART_BUTTON is not presented on product page"
        link = self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()

    def correct_cost_in_cart(self):
        a = self.driver.find_element('xpath', '//*[@id="content_inner"]/article/table/tbody/tr[4]/td').text
        b = self.driver.find_element('xpath', '/html/body/header/div[1]/div/div[2]').text
        assert a in b

    def correct_product_added(self):
        a = self.driver.find_element('xpath', '//*[@id="content_inner"]/article/div[1]/div[2]/h1').text
        b = self.driver.find_element('xpath', '//*[@id="messages"]/div[1]/div/strong').text
        assert a == b, 'product did not add to cart'
