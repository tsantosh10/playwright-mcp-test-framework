import pytest
import json
from pathlib import Path
from pages.login_page import LoginPage


class TestImedxLogin:
    """Test suite for iMedx Login Page - https://san-hcs-dev.imedx.com.au"""

    @pytest.fixture(scope="class")
    def test_data(self):
        """Load test data from JSON file"""
        data_file = Path("test_data/login_test_data.json")
        with open(data_file, "r") as f:
            return json.load(f)

    def test_valid_login_with_valid_credentials(self, page, app_settings, test_data):
        """
        Test: User can successfully login with valid credentials
        - Username: Sai
        - Password: Imedx@123
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Get valid credentials from test data
        valid_user = test_data["valid_user"]
        
        # Perform login
        login_page.login(valid_user["username"], valid_user["password"])
        
        # Verify successful login
        login_page.verify_login_success()
        
        # Additional verification - check URL doesn't contain 'login'
        current_url = login_page.get_current_url()
        assert "login" not in current_url.lower(), f"Login failed, still on: {current_url}"

    def test_invalid_login_with_wrong_password(self, page, app_settings, test_data):
        """
        Test: Login fails with invalid password
        - Username: Sai
        - Password: WrongPassword
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Attempt login with wrong password
        login_page.login(test_data["valid_user"]["username"], "WrongPassword")
        
        # Wait for error to appear
        page.wait_for_timeout(2000)
        
        # Check that we're still on login page
        current_url = login_page.get_current_url()
        assert "login" in current_url.lower() or page.query_selector(login_page.ERROR_MESSAGE), \
            "Error not shown for invalid password"

    def test_invalid_login_with_wrong_credentials(self, page, app_settings, test_data):
        """
        Test: Login fails with completely wrong credentials
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Attempt login with wrong credentials
        invalid_user = test_data["invalid_user"]
        login_page.login(invalid_user["username"], invalid_user["password"])
        
        # Wait for error to appear
        page.wait_for_timeout(2000)
        
        # Verify we're still on login page
        current_url = login_page.get_current_url()
        assert "login" in current_url.lower() or page.query_selector(login_page.ERROR_MESSAGE), \
            "Error not shown for invalid credentials"

    def test_empty_username_login_attempt(self, page, app_settings):
        """
        Test: Login fails when username field is empty
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Attempt login with empty username
        login_page.login("", "Imedx@123")
        
        # Wait for validation error
        page.wait_for_timeout(1000)
        
        # Check we're still on login page
        current_url = login_page.get_current_url()
        assert "login" in current_url.lower(), "Login should fail with empty username"

    def test_empty_password_login_attempt(self, page, app_settings):
        """
        Test: Login fails when password field is empty
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Attempt login with empty password
        login_page.login("Sai", "")
        
        # Wait for validation error
        page.wait_for_timeout(1000)
        
        # Check we're still on login page
        current_url = login_page.get_current_url()
        assert "login" in current_url.lower(), "Login should fail with empty password"

    def test_page_elements_visibility(self, page, app_settings):
        """
        Test: Verify all login page elements are visible
        - Username input field
        - Password input field
        - Login button
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Check if elements are present
        username_field = page.query_selector(login_page.USERNAME_INPUT)
        password_field = page.query_selector(login_page.PASSWORD_INPUT)
        login_button = page.query_selector(login_page.LOGIN_BUTTON)
        
        assert username_field is not None, "Username input field not found"
        assert password_field is not None, "Password input field not found"
        assert login_button is not None, "Login button not found"

    def test_password_field_is_masked(self, page, app_settings):
        """
        Test: Verify password field is masked (type='password')
        """
        login_page = LoginPage(page)
        
        # Navigate to login page
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        
        # Find password field and verify it's type password
        password_field = page.query_selector(login_page.PASSWORD_INPUT)
        password_type = password_field.get_attribute("type") if password_field else None
        
        assert password_type == "password", "Password field should be masked"

    def test_successful_login_navigation(self, page, app_settings, test_data):
        """
        Test: Verify page navigates after successful login
        """
        login_page = LoginPage(page)
        
        # Get initial URL
        login_page.open_login_page(app_settings.base_url)
        login_page.wait_for_page_load()
        initial_url = login_page.get_current_url()
        
        # Perform login
        valid_user = test_data["valid_user"]
        login_page.login(valid_user["username"], valid_user["password"])
        
        # Wait for navigation
        page.wait_for_timeout(3000)
        
        # Get final URL
        final_url = login_page.get_current_url()
        
        # URLs should be different (navigation occurred)
        assert initial_url != final_url, f"Navigation did not occur. Same URL: {initial_url}"
        assert "login" not in final_url.lower(), f"Still on login page: {final_url}"
