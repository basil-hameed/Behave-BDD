from selenium.webdriver.common.by import By

class Locators:
    # Login Page Locators
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    error_msg = (By.XPATH, '//h3[@data-test="error"]')