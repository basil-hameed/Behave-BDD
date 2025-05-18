from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.web_locators import Locators
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # method to perform login, needs credentials
    def enter_credentials(self, username, password):
        self.wait.until(EC.visibility_of_element_located(Locators.username_field)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(Locators.password_field)).send_keys(password)

    # method to click login button
    def login(self):
        self.wait.until(EC.element_to_be_clickable(Locators.login_button)).click()

    # method to verify error displayed
    def is_error_displayed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(Locators.error_message)).is_displayed()
        except TimeoutException:
            return False