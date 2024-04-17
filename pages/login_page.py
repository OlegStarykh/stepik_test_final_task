from .base_page import BasePage
from .lokators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login link is not presented on login page"
        # assert 'Log In' in self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).value, 'Not presented login button on login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_POLE_LOG), 'Email pole is not presented'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_POLE_LOG), 'Password pole log is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_POLE_REG), 'Email pole is not presented on registration'
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_POLE_REG), 'Password pole is not presented on registration'
        assert self.is_element_present(
            *LoginPageLocators.CONFIRM_PASSWORD_POLE_REG), 'Confirm password pole is not presented on registration'

    def register_new_user(self, email, password):
        self.driver.find_element(*LoginPageLocators.EMAIL_POLE_REG).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_POLE_REG).send_keys(password)
        self.driver.find_element(*LoginPageLocators.CONFIRM_PASSWORD_POLE_REG).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def register_new_fake_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = 'Qwertyuiop000'
        self.driver.find_element(*LoginPageLocators.EMAIL_POLE_REG).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_POLE_REG).send_keys(password)
        self.driver.find_element(*LoginPageLocators.CONFIRM_PASSWORD_POLE_REG).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
