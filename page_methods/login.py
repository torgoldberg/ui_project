from page_methods.base import Base
from utils.locators import LoginPageLocators


class Login(Base):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def check_login_page_loaded(self):
        """
        Click the login button and check if the login page is loaded
        """
        login = self.wait_for_element(*self.locator.LOGIN_PROCESS_BUTTON)
        self.click_element(element=login)
        self.wait_for_element(*self.locator.LOGIN_LOGO)

    def enter_login_data(self, email, password):
        """
        Enter the email and password, and submit the login form.
        """
        email_locator = self.wait_for_element(*self.locator.EMAIL)
        self.write_to_element(element=email_locator, word=email)
        password_locator = self.wait_for_element(*self.locator.PASSWORD)
        self.write_to_element(element=password_locator, word=password)
        submit = self.wait_for_element(*self.locator.SUBMIT)
        self.click_element(element=submit)

    def invalid_credentials_error(self):
        """
        Submit the login form and check for invalid credentials error
        """
        submit = self.wait_for_element(*self.locator.SUBMIT)
        self.click_element(element=submit)
        invalid_error_element = self.wait_for_element(*self.locator.ERROR)
        self.wait_for_element(*self.locator.LOGIN_LOGO)
        return invalid_error_element

    def close_login_page(self):
        """
        Close the login page by clicking the close button
        """
        close = self.wait_for_element(*self.locator.CLOSE)
        self.click_element(element=close)


