import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

TEST_EMAIL = 'HASFSAF@gmail.com'
TEST_PASSWORD = 'Bababa123@'


class PrerequisiteSetup(unittest.TestCase):

    @staticmethod
    def initialise_user():
        url = 'https://gizmo.rakuten.tv/v3/me'
        headers = {
            'content-type': 'application/json',
            "authority": "gizmo.rakuten.tv",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "*/*"
        }
        emailAndName = TEST_EMAIL
        password = TEST_PASSWORD
        data = {
            "user": {
                "email": emailAndName,
                "password": TEST_PASSWORD,
                "password_confirmation": TEST_PASSWORD,
                "username": emailAndName
            },
            "marketing_opt_in": False,
            "terms_conditions_ids": "3921,3923,3929",
            "device_identifier": "web",
            "device_metadata": {
                "app_version": "v5.3.6",
                "audio_quality": "2.0",
                "brand": "chrome",
                "firmware": "XX.XX.XX",
                "hdr": False,
                "model": "GENERIC",
                "os": "Mac OS",
                "sdk": "116.0.0",
                "serial_number": "not implemented",
                "trusted_uid": False,
                "uid": "4f90da2c-9cd6-4b17-a48d-411d4cc41fa6",
                "video_quality": "FHD",
                "year": 1970
            },
            "ifa_id": "182110ba-59e8-491d-b7d4-30191832aa21"
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print("Request was successful.")
        else:
            Exception(f"Request failed with status code {response.status_code}.")
        return emailAndName, password

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.delete_all_cookies()
        cls.driver.get("https://www.rakuten.tv/es")
        delay = 3

    @classmethod
    def tearDown(cls):
        cls.driver.close()
