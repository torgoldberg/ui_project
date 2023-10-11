from methods.base_methods import BaseMethods
from utils.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BaseMethods):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)

    def check_login_page_loaded(self):
        login = self.find_element(*self.locator.LOGIN_PROCESS_BUTTON)
        login.click()
        return True if self.find_element(*self.locator.LOGIN_LOGO) else False

    def enter_login_data(self, email, password):
        email_locator = self.find_element(*self.locator.EMAIL)
        self.write_to_element(element=email_locator, word=email)
        password_locator = self.find_element(*self.locator.PASSWORD)
        self.write_to_element(element=password_locator, word=password)
        submit = self.find_element(*self.locator.SUBMIT)
        submit.click()

    def invalid_credentials_error(self):
        submit = self.find_element(*self.locator.SUBMIT)
        submit.click()
        self.find_element(*self.locator.ERROR)
        return True if self.find_element(*self.locator.LOGIN_LOGO) else False

    def close_login_page(self):
        close = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.locator.CLOSE))
        close.click()

