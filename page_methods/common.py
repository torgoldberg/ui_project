from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import random
import string
from utils.locators import PopupPageLocators
import re
from utils.api_data import *
import requests
from selenium.webdriver.common.action_chains import ActionChains


class common(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        """
        Find element, use webdriver
        """
        return self.driver.find_element(*locator)

    def wait_for_element(self, *locator):
        """
        Find a specific element in the page
        """
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except NoSuchElementException as e:
            raise NoSuchElementException(f"{locator} not found. Original message: {e}")
        except TimeoutException as e:
            raise TimeoutException(f"{self.timeout} timeout waiting for element. Original message: {e}")

    def check_element_no_longer_available(self, locator):
        """
        Check a specific element in the page no longer available
        """
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            wait.until(EC.invisibility_of_element_located(locator))
        except:
            raise Exception(f"Element is still visible after waiting for {self.timeout} seconds.")

    def close_cookies_popup(self):
        """
        Close the cookies pop up window when opening the website
        """
        wait = WebDriverWait(self.driver, self.timeout)
        iframe_element = wait.until(EC.visibility_of_element_located(PopupPageLocators.COOKIES_FRAME))
        self.driver.switch_to.frame(iframe_element)
        accept_button = wait.until(EC.visibility_of_element_located(PopupPageLocators.ACCEPT_COOKIES))
        accept_button.click()
        self.driver.switch_to.default_content()

    @staticmethod
    def initialise_user():
        """
        Initialize user data and make a POST request to a specific URL
        """
        url = 'https://gizmo.rakuten.tv/v3/me'
        emailAndName = TEST_EMAIL
        password = TEST_PASSWORD
        data = DATA
        headers = HEADERS
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"Api request finish with success")
        else:
            Exception(f"Request failed with status code {response.status_code}.")
        return emailAndName, password

    def click_element(self, element):
        """
        Click element in the page
        """
        try:
            wait = WebDriverWait(element.parent, self.timeout)
            wait.until(EC.element_to_be_clickable(element))
            element.click()
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f"Failed to click the element. Original message: {e}")

    @staticmethod
    def compere_text(first_word, second_word):
        """
        Compare two text elements
        """
        regex = re.compile('[“”"‘’\'`]')
        first_word = regex.sub('', first_word)
        second_word = regex.sub('', second_word)
        if first_word != second_word:
            raise ValueError(f"Text elements: {first_word} don't match: {second_word}")

    @staticmethod
    def get_user_data():
        """
        Generate a random user data
        """
        user_email = common.generate_random_email()
        user_password = common.generate_random_string()
        return user_email, user_password

    @staticmethod
    def write_to_element(element, word):
        """
        Writing to element some word
        """
        try:
            element.send_keys(word)
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f"Failed to write '{word}' to the element. Original message: {str(e)}")
        except StaleElementReferenceException as e:
            raise StaleElementReferenceException(f"The element is no longer valid. Original message: {e}")

    @staticmethod
    def generate_random_email():
        """
        Generate a random email address
        """
        domain = 'gmail.com'
        random_email_string_length = 10
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
        random_email = random_string + '@' + domain
        return random_email

    @staticmethod
    def generate_random_string():
        """
        Generate a random string with uppercase, lowercase and @
        """
        characters = string.ascii_letters + "@_"
        random_string = ''.join(random.choices(characters, k=10))
        return random_string

    def hover(self, locator):
        """
        Hover a specific element
        """
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
