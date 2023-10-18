from page_methods.common import common
from utils.locators import *


class Registration(common):
    def __init__(self, driver):
        self.locator = RegistrationPageLocators
        super().__init__(driver)

    def check_registration_page_loaded(self):
        """
        Click the registration button to load the registration page
        """
        registration = self.wait_for_element(*self.locator.REGISTRATION_PROCESS_BUTTON)
        self.click_element(element=registration)

    def enter_registration_data(self):
        """
        Enter registration data, agree to terms of condition, and submit the registration form
        """
        data = common.get_user_data()
        email = self.wait_for_element(*self.locator.EMAIL)
        self.write_to_element(element=email, word=data[0])
        password = self.wait_for_element(*self.locator.PASSWORD)
        self.write_to_element(element=password, word=data[1])
        terms_of_condition = self.wait_for_element(*self.locator.CONDITION)
        self.driver.execute_script("arguments[0].click();", terms_of_condition)
        create = self.wait_for_element(*self.locator.CONFIRM)
        self.click_element(element=create)
        return data


