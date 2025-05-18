from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.web_locators import Locators

class LoginPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def navigate_login_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_credentials(self, username, password):
        self.wait.until(EC.visibility_of_element_located(Locators.username_field)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(Locators.password_field)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(Locators.login_button)).click()

    def is_dashboard_present(self):
        try:
            self.wait.until(EC.presence_of_element_located(Locators.dashboard))
            return True
        except TimeoutException:
            return False

    def is_login_failed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(Locators.error_message))
            return True
        except TimeoutException:
            return False
