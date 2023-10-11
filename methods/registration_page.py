from methods.base_methods import BaseMethods
from utils.locators import *


class RegistrationPage(BaseMethods):
    def __init__(self, driver):
        self.locator = RegistrationPageLocators
        super().__init__(driver)

    def check_registration_page_loaded(self):
        registration = self.find_element(*self.locator.REGISTRATION_PROCESS_BUTTON)
        registration.click()
        return True if self.find_element(*self.locator.REGISTRATION_LOGO) else False

    def enter_registration_data(self):
        data = BaseMethods.get_user_data(self)
        email = self.find_element(*self.locator.EMAIL)
        self.write_to_element(element=email, word=data[0])
        password = self.find_element(*self.locator.PASSWORD)
        self.write_to_element(element=password, word=data[1])
        terms_of_condition = self.find_element(*self.locator.CONDITION)
        self.driver.execute_script("arguments[0].click();", terms_of_condition)
        create = self.find_element(*self.locator.CONFIRM)
        create.click()
        return data


