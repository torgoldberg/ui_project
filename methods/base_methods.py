from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import random
import string
from utils.locators import PopupPageLocators


class BaseMethods(object):
    def __init__(self, driver, base_url='https://www.rakuten.tv/es'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        """
        Find element in the html
        """
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element
        except (NoSuchElementException, TimeoutException):
            return None

    def close_cookies_popup(self):
        """
        Close the cookies pop up window
        """
        wait = WebDriverWait(self.driver, 30)
        iframe_element = wait.until(EC.visibility_of_element_located(PopupPageLocators.COOKIES_FRAME))
        self.driver.switch_to.frame(iframe_element)
        accept_button = wait.until(EC.visibility_of_element_located(PopupPageLocators.ACCEPT_COOKIES))
        accept_button.click()
        self.driver.switch_to.default_content()

    def get_user_data(self):
        """
        Generate a random user data
        """
        user_email = self.generate_random_email()
        user_password = self.generate_random_string()
        return user_email, user_password

    def write_to_element(self, element, word):
        """
        filling the search bar with a word
        """
        element.send_keys(word)

    def generate_random_email(self):
        """
        Generate a random email address
        """
        domain = 'gmail.com'
        random_email_string_length = 10
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
        random_email = random_string + '@' + domain
        return random_email

    def generate_random_string(self):
        """
        Generate a random string with uppercase, lowercase and @
        """
        characters = string.ascii_letters + "@_"
        random_string = ''.join(random.choices(characters, k=10))
        return random_string
