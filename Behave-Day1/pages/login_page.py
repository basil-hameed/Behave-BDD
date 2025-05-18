from locators.web_locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self, username, password):
        self.driver.find_element(*Locators.username_field).send_keys(username)
        self.driver.find_element(*Locators.password_field).send_keys(password)

    def login(self):
        self.driver.find_element(*Locators.login_button).click()

    def is_error_displayed(self):
        return self.driver.find_element(*Locators.error_msg).is_displayed()