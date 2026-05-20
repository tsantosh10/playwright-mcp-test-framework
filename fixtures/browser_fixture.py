import pytest
from playwright.sync_api import sync_playwright
from config.settings import Settings


@pytest.fixture(scope="session")
def app_settings():
    return Settings(env="dev")


@pytest.fixture(scope="function")
def page(app_settings):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, app_settings.browser)
        browser = browser_type.launch(headless=app_settings.headless)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()
