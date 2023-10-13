import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_methods.main import Main
import logging


class TestPrerequisite(unittest.TestCase):

    def setUp(self):
        """
        Set up the WebDriver and navigate to a web page
        """
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.delete_all_cookies()
        self.driver.get("https://www.rakuten.tv/es")
        delay = 3
        page = Main(self.driver)
        page.check_main_page_loaded()
        logging.basicConfig(level=logging.INFO)
        self.emailAndName = ""
        self.password = ""

    def tearDown(self):
        """
        Clean up resources by closing the WebDriver
        """
        self.driver.delete_all_cookies()
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase()
    unittest.TextTestRunner(verbosity=1).run(suite)

