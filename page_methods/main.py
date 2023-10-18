from page_methods.common import common
from utils.locators import *


class Main(common):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_main_page_loaded(self):
        """
        Close the cookies popup and check if the main page is loaded
        """
        common.close_cookies_popup(self)
        self.wait_for_element(*self.locator.HOME_LOGO)

    def check_connected_user(self, email):
        """
        Check if the connected user's email matches the given email
        """
        connected_user = self.wait_for_element(*self.locator.LOGIN_USER)
        self.compere_text(first_word=email, second_word=connected_user.text)

    def write_to_search_bar(self, word):
        """
        Enter a search word in the search bar
        """
        search_locator = self.wait_for_element(*self.locator.SEARCH)
        self.write_to_element(element=search_locator, word=word)

    def check_after_search(self, text):
        """
        Check if the displayed search results text matches the expected text
        """
        element = self.wait_for_element(*self.locator.RESULTS)
        self.compere_text(first_word=text, second_word=element.text)

    def hover_connected_user_profile(self):
        """
        Click the connected user profile
        """
        self.hover(self.locator.LOGIN_USER)

    def select_logout_options_menu(self):
        """
        Log out the connected user
        """
        logout_element = self.driver.find_element(*self.locator.USER_LOGOUT)
        self.click_element(logout_element)


