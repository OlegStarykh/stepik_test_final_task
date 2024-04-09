
class MainPageLocators:
    LOGIN_LINK = ('xpath', '//*[@id="login_link"]')


class LoginPageLocators:
    LOGIN_BUTTON = ('xpath', '//*[@id="login_form"]/button')
    EMAIL_POLE_LOG = ('xpath', '//*[@id="id_login-username"]')
    PASSWORD_POLE_LOG = ('xpath', '//*[@id="id_login-password"]')
    EMAIL_POLE_REG = ('xpath', '//*[@id="id_registration-email"]')
    PASSWORD_POLE_REG = ('xpath', '//*[@id="id_login-password"]')
    CONFIRM_PASSWORD_POLE_REG = ('xpath', '//*[@id="id_registration-password2"]')

