from selenium.webdriver.common.by import By

class Locators:
    username_field = (By.NAME , 'username')
    password_field = (By.NAME , 'password')
    login_button = (By.XPATH , '//button[text()=" Login "]')
    error_message = (By.XPATH , '//p[text()="Invalid credentials"]')