from .base_page import BasePage
from .locators import LoginPagesLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPagesLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPagesLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPagesLocators.REGISTRATION_EMAIL_FORM).send_keys(email)
        self.browser.find_element(*LoginPagesLocators.REGISTRATION_PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*LoginPagesLocators.CONFIRM_PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*LoginPagesLocators.REGISTRATION_BUTTON).click()
