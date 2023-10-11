from selenium.webdriver.common.by import By


class PopupPageLocators(object):
    """
    Hold all popup page elements
    """
    ACCEPT_COOKIES = (By.ID, "save")
    COOKIES_FRAME = (By.ID, "gdpr-consent-notice")


class MainPageLocators(object):
    """
    Hold all main page elements
    """
    HOME_LOGO = (By.XPATH, "//title[text()='Inicio - Rakuten TV']")
    LOGIN_USER = (By.CSS_SELECTOR, "span.styles__StyledMenuUserName-sc-kzgvyp-5")
    SEARCH = (By.CSS_SELECTOR, 'input[data-testid="search-input"]')
    RESULTS = (By.CSS_SELECTOR, 'h3.styles__StyledSearchResultsText-sc-94hniz-2')


class RegistrationPageLocators(object):
    """
    Hold all registration page elements
    """
    REGISTRATION_PROCESS_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="register-menu-link"]')
    REGISTRATION_LOGO = (By.XPATH, "//span[contains(text(),'Crear cuenta')]")
    PASSWORD = (By.ID, "password")
    EMAIL = (By.ID, "email")
    CONDITION = (By.ID, "termsAndConditions")
    CONFIRM = (By.XPATH, "//button[@name='Crear cuenta']")


class LoginPageLocators(object):
    """
    Hold all login page elements
    """
    LOGIN_PROCESS_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="login-menu-link"]')
    LOGIN_LOGO = (By.XPATH, "//h2[text()='Iniciar sesión']")
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.NAME, 'Iniciar sesión')
    ERROR = (By.ID, 'WARNING_FILLED')
    CLOSE = (By.CSS_SELECTOR, 'button[data-testid="modal_close_button"]')

