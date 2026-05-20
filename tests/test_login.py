from pages.login_page import LoginPage


def test_valid_login(page, app_settings):
    login_page = LoginPage(page)
    login_page.open_login_page(app_settings.base_url)
    login_page.login("admin", "admin123")
    login_page.verify_login_success()


def test_invalid_login(page, app_settings):
    login_page = LoginPage(page)
    login_page.open_login_page(app_settings.base_url)
    login_page.login("wrong_user", "wrong_password")
    login_page.verify_login_error()
