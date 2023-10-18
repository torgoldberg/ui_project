from page_methods.login import Login
from page_methods.main import Main
from page_methods.registration import Registration
import logging as logger
from tests.test_prerequisite import TestPrerequisite
from page_methods.common import common


class TestMain(TestPrerequisite):

    def test_01_page_load(self):
        page = Main(self.driver)
        page.check_main_page_loaded()
        logger.info(f"Load the main page title finish with success")

    def test_02_registration(self):
        page = Main(self.driver)
        page.check_main_page_loaded()
        page = Registration(self.driver)
        page.check_registration_page_loaded()
        self.registered_email, self.registered_password = page.enter_registration_data()
        self.emailAndName = self.registered_email
        self.password = self.registered_password
        page = Main(self.driver)
        page.check_connected_user(email=self.registered_email)
        logger.info(f"Registered a new user finish with success")

    def test_03_login(self):
        page = Main(self.driver)
        page.check_main_page_loaded()
        page = Login(self.driver)
        page.check_login_page_loaded()
        page.enter_login_data(email=self.emailAndName, password=self.password)
        logger.info("Login process finish with success")

    def test_04_invalid_login(self):
        page = Main(self.driver)
        page.check_main_page_loaded()
        ApiEmailAndName, ApiPassword = common.initialise_user()
        page = Login(self.driver)
        page.check_login_page_loaded()
        page.enter_login_data(email=ApiEmailAndName, password=ApiPassword)
        invalid_email_data = ["123456@gmail.com"]
        invalid_password_data = ["12345678"]
        page = Main(self.driver)
        page.check_connected_user(email=ApiEmailAndName)
        page.hover_connected_user_profile()
        page.select_logout_options_menu()
        for i in invalid_email_data:
            page = Login(self.driver)
            page.check_login_page_loaded()
            page.enter_login_data(email=i, password=ApiPassword)
            error = page.invalid_credentials_error()
            page.close_login_page()
            page.check_element_no_longer_available(locator=error)
        for i in invalid_password_data:
            page = Login(self.driver)
            page.check_login_page_loaded()
            page.enter_login_data(email=ApiEmailAndName, password=i)
            error = page.invalid_credentials_error()
            page.close_login_page()
            page.check_element_no_longer_available(locator=error)
        logger.info("Test invalid login finish with success")

    def test_05_search(self):
        page = Main(self.driver)
        page.check_main_page_loaded()
        search_word = "Guerra de las Galaxias"
        page.write_to_search_bar(word=search_word)
        page.check_after_search(text=f'Resultados de: "{search_word}"')
        logger.info(f"Search result finish with success")
