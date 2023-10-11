import unittest
from methods.login_page import LoginPage
from methods.main_page import MainPage
from methods.registration_page import RegistrationPage
from tests.prerequisite_setup import PrerequisiteSetup
import logging as logger
import logging_config  # Import the logging configuration


class TestMain(PrerequisiteSetup):

    def setUp(self):
        page = MainPage(self.driver)
        self.assertTrue(page.check_main_page_loaded())

    def test_page_load(self):
        logger.info(f"we load the main page title with success")

    def test_registration(self):
        page = RegistrationPage(self.driver)
        page.check_registration_page_loaded()
        self.registered_email, self.registered_password = page.enter_registration_data()
        page = MainPage(self.driver)
        page.check_connected_user(email=self.registered_email)
        logger.info(f"we registered a new user with success")

    def test_login(self):
        emailAndName, password = PrerequisiteSetup.initialise_user()
        page = LoginPage(self.driver)
        page.check_login_page_loaded()
        page.enter_login_data(email=emailAndName, password=password)
        logger.info("we login with success")

    def test_invalid_login(self):
        emailAndName, password = PrerequisiteSetup.initialise_user()
        invalid_email_data = ["123456@gmail.com"]
        invalid_password_data = ["12345678"]
        for i in invalid_email_data:
            page = LoginPage(self.driver)
            page.check_login_page_loaded()
            page.enter_login_data(email=i, password=password)
            page.invalid_credentials_error()
            page.close_login_page()
        for i in invalid_password_data:
            page = LoginPage(self.driver)
            page.check_login_page_loaded()
            page.enter_login_data(email=emailAndName, password=i)
            page.invalid_credentials_error()
            page.close_login_page()
        logger.info("we test invalid login with success")

    def test_search(self):
        page = MainPage(self.driver)
        search_word = "Guerra de las Galaxias"
        page.write_to_search_bar(word=search_word)
        page.check_after_search(text="Resultados de: “Guerra de las Galaxias")
        logger.info("search result finish with success")


if __name__ == "__main__":
    unittest.main()
