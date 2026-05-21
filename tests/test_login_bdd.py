import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios('../features/login.feature')

@given('the login page is opened', target_fixture="open_login_page")
def open_login_page(page, app_settings):
    login_page = LoginPage(page)
    login_page.open_login_page(app_settings.base_url)
    login_page.wait_for_page_load()
    return login_page

@when(parsers.re(r'the user logs in with username "(?P<username>.*)" and password "(?P<password>.*)"'))
def user_logs_in(open_login_page, username, password):
    login_page = open_login_page
    login_page.login(username, password)

@then('the user should be logged in successfully')
def user_logged_in(open_login_page, page):
    login_page = open_login_page
    login_page.verify_login_success()
    # extra check: URL changed
    assert 'login' not in page.url.lower()

@then('the login should fail with an error message')
def login_should_fail(open_login_page, page):
    login_page = open_login_page
    login_page.verify_login_failed()

@then('the login should fail with validation error')
def login_validation_error(open_login_page, page):
    login_page = open_login_page
    login_page.verify_login_failed()
