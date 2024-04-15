
class MainPageLocators:
    LOGIN_LINK = ('xpath', '//*[@id="login_link"]')


class LoginPageLocators:
    LOGIN_BUTTON = ('xpath', '//*[@id="login_form"]/button')
    EMAIL_POLE_LOG = ('xpath', '//*[@id="id_login-username"]')
    PASSWORD_POLE_LOG = ('xpath', '//*[@id="id_login-password"]')
    EMAIL_POLE_REG = ('xpath', '//*[@id="id_registration-email"]')
    PASSWORD_POLE_REG = ('xpath', '//*[@id="id_login-password"]')
    CONFIRM_PASSWORD_POLE_REG = ('xpath', '//*[@id="id_registration-password2"]')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = ('xpath', '//*[@id="add_to_basket_form"]/button')
    SUCCESS_MESSAGE = ('xpath', '(//*[@id="messages"]/div[1]/div/text())[2]')


class BasePageLocators:
    LOGIN_LINK = ('xpath', '//*[@id="login_link"]')
    BASKET_BUTTON = ('xpath', '//*[@id="default"]/header/div[1]/div/div[2]/span/a')


class BasketPageLocators:
    TOTAL_BASKET_PRICE = ('xpath', '//*[@id="basket_formset"]/div/div/div[5]/p/text()')

