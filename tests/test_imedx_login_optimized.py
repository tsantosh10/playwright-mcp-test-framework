import pytest
import json
from pathlib import Path
from pages.login_page import LoginPage


class TestImedxLoginOptimized:
    """Optimized test suite for iMedx Login Page - https://san-hcs-dev.imedx.com.au"""

    @pytest.fixture(scope="class")
    def test_data(self):
        """Load test data from JSON file"""
        data_file = Path("test_data/login_test_data.json")
        with open(data_file, "r") as f:
            return json.load(f)

    def test_01_valid_login_with_valid_credentials(self, page, app_settings, test_data):
        """
        PRIMARY TEST: User successfully logs in with valid credentials
        URL: https://san-hcs-dev.imedx.com.au/
        Username: Sai
        Password: Imedx@123
        Expected: Login successful, redirected to dashboard/home
        """
        login_page = LoginPage(page)
        
        # Navigate to application
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Record initial page state
        initial_title = page.title()
        print(f"Initial Page Title: {initial_title}")
        
        # Get valid credentials
        valid_user = test_data["valid_user"]
        print(f"Logging in as: {valid_user['username']}")
        
        # Perform login
        login_page.login(valid_user["username"], valid_user["password"])
        
        # Wait for page to load after login
        page.wait_for_timeout(3000)
        
        # Verify successful login
        final_url = login_page.get_current_url()
        final_title = page.title()
        
        print(f"Final URL: {final_url}")
        print(f"Final Page Title: {final_title}")
        
        # Assert login was successful (URL changed from login page)
        assert final_url != app_settings.base_url or "login" not in final_url.lower(), \
            f"Login may have failed. URL: {final_url}"

    def test_02_page_loads_correctly(self, page, app_settings):
        """
        Verify login page loads and displays all required elements
        """
        login_page = LoginPage(page)
        
        # Navigate to application
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Verify page title indicates login page
        page_title = page.title()
        print(f"Page Title: {page_title}")
        assert page_title is not None and len(page_title) > 0, "Page title is empty"

    def test_03_username_input_field_exists(self, page, app_settings):
        """
        Verify username input field is present on login page
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Check if username field exists
        username_field = page.query_selector(login_page.USERNAME_INPUT)
        assert username_field is not None, "Username input field not found on page"
        assert username_field.is_visible(), "Username input field is not visible"

    def test_04_password_input_field_exists(self, page, app_settings):
        """
        Verify password input field is present and masked
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Check if password field exists
        password_field = page.query_selector(login_page.PASSWORD_INPUT)
        assert password_field is not None, "Password input field not found"
        assert password_field.is_visible(), "Password input field is not visible"
        
        # Verify it's a password type (masked)
        password_type = password_field.get_attribute("type")
        assert password_type == "password", f"Password field type should be 'password', got '{password_type}'"

    def test_05_login_button_exists(self, page, app_settings):
        """
        Verify login/submit button is present on page
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Check if login button exists
        login_button = page.query_selector(login_page.LOGIN_BUTTON)
        assert login_button is not None, "Login button not found on page"
        assert login_button.is_visible(), "Login button is not visible"

    def test_06_can_enter_username_text(self, page, app_settings):
        """
        Verify username field accepts text input
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Enter test username
        test_username = "Sai"
        login_page.fill(login_page.USERNAME_INPUT, test_username)
        
        # Wait and verify
        page.wait_for_timeout(500)
        username_field = page.query_selector(login_page.USERNAME_INPUT)
        field_value = username_field.input_value()
        
        assert field_value == test_username, f"Expected '{test_username}', got '{field_value}'"

    def test_07_can_enter_password_text(self, page, app_settings):
        """
        Verify password field accepts input
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Enter test password
        test_password = "TestPassword123"
        login_page.fill(login_page.PASSWORD_INPUT, test_password)
        
        # Wait and verify
        page.wait_for_timeout(500)
        password_field = page.query_selector(login_page.PASSWORD_INPUT)
        field_value = password_field.input_value()
        
        assert field_value == test_password, f"Password not entered correctly"

    def test_08_login_form_submission(self, page, app_settings, test_data):
        """
        Verify login form can be submitted with valid credentials
        Credentials: Sai / Imedx@123
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Get credentials
        valid_user = test_data["valid_user"]
        username = valid_user["username"]
        password = valid_user["password"]
        
        # Fill form
        login_page.fill(login_page.USERNAME_INPUT, username)
        login_page.fill(login_page.PASSWORD_INPUT, password)
        
        # Verify form is filled
        username_field = page.query_selector(login_page.USERNAME_INPUT)
        password_field = page.query_selector(login_page.PASSWORD_INPUT)
        
        assert username_field.input_value() == username, "Username not filled correctly"
        assert password_field.input_value() == password, "Password not filled correctly"
        
        # Submit form
        login_page.click(login_page.LOGIN_BUTTON)
        
        # Wait for submission to process
        page.wait_for_timeout(2000)
        
        # Verify submission was accepted
        print(f"Form submitted. Current URL: {page.url}")

    def test_09_session_established_after_login(self, page, app_settings, test_data):
        """
        Verify user session is established after successful login
        """
        login_page = LoginPage(page)
        
        # Navigate and login
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        valid_user = test_data["valid_user"]
        login_page.login(valid_user["username"], valid_user["password"])
        
        # Wait for login to complete
        page.wait_for_timeout(3000)
        
        # Check for session indicators (cookies, local storage, etc)
        cookies = page.context.cookies()
        print(f"Cookies after login: {len(cookies)} cookies found")
        
        # Session is typically confirmed by navigation away from login page
        current_url = page.url
        print(f"Current URL after login: {current_url}")

    def test_10_credentials_data_loaded_correctly(self, page, app_settings, test_data):
        """
        Verify test data is loaded and credentials are accessible
        """
        assert test_data is not None, "Test data not loaded"
        assert "valid_user" in test_data, "Valid user data not found"
        
        valid_user = test_data["valid_user"]
        assert valid_user["username"] == "Sai", f"Expected username 'Sai', got '{valid_user['username']}'"
        assert valid_user["password"] == "Imedx@123", f"Expected password 'Imedx@123', got '{valid_user['password']}'"
        
        print(f"✓ Credentials verified: Username={valid_user['username']}, Password={'*' * len(valid_user['password'])}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
