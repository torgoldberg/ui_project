from methods.base_methods import BaseMethods
from utils.locators import *


class MainPage(BaseMethods):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_main_page_loaded(self):
        BaseMethods.close_cookies_popup(self)
        return True if self.find_element(*self.locator.HOME_LOGO) else False

    def check_connected_user(self, email):
        connected_user = self.find_element(*self.locator.LOGIN_USER)
        if email != connected_user.text:
            raise AssertionError(f"Emails do not match: {email} != {connected_user.text}")

    def write_to_search_bar(self, word):
        search_locator = self.find_element(*self.locator.SEARCH)
        self.write_to_element(element=search_locator, word=word)

    def check_after_search(self, text):
        element = self.find_element(*self.locator.RESULTS)
        result_text = element.text
        if result_text != text:
            Exception(f"expected text for search result is wrong")
