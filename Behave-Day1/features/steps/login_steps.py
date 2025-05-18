# import all dependencies

from behave import given, when, then
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given("I am on the sauce demo login page")
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.saucedemo.com/")
    context.page = LoginPage(context.driver)

@when("I enter valid username and password")
def step_impl(context):
    context.page.enter_credentials("standard_user", "secret_sauce")

@when("I enter invalid username and password")
def step_impl(context):
    context.page.enter_credentials("invaliduser", "invalidpass")

@when("I click the login button")
def step_impl(context):
    context.page.login()

@then("I should be redirected to the inventory page")
def step_impl(context):
    assert "inventory" in context.driver.current_url
    context.driver.quit()

@then("I should see an error message")
def step_impl(context):
    assert context.page.is_error_displayed()
    context.driver.quit()