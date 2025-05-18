from behave import given, when, then
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given("the user is on the OrangeHRM login page")
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.page = LoginPage(context.driver)
    context.page.navigate_login_page()

@when('the user enters username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.page.enter_credentials(username, password)

@when('the user click login button')
def step_impl(context):
    context.page.click_login()

@then('login should "{result}"')
def step_impl(context, result):
    if result == "success":
        assert context.page.is_dashboard_present, "Expected dashboard after login"
        context.driver.quit()
    else:
        assert context.page.is_login_failed(), "Expected error message"
        context.driver.quit()