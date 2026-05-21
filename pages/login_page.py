from pages.base_page import BasePage


class LoginPage(BasePage):
    # Updated locators for iMedx application
    USERNAME_INPUT = 'input[type="email"], input[name="username"], input[id*="user"], input[placeholder*="mail"]'
    PASSWORD_INPUT = 'input[type="password"]'
    LOGIN_BUTTON = 'button:has-text("Login"), button[type="submit"], button:has-text("Sign In")'
    ERROR_MESSAGE = '.error-message, [role="alert"], .alert-error, [class*="error"]'
    DASHBOARD_HEADER = 'h1, [role="heading"], [class*="dashboard"], [class*="welcome"]'
    LOADING_SPINNER = '[class*="spinner"], [class*="loading"], .loader'

    def open_login_page(self, base_url: str):
        """Navigate to the login page"""
        self.navigate(base_url)
        page_title = self.page.title()
        print(f"Page Title: {page_title}")

    def login(self, username: str, password: str):
        """Fill in credentials and submit login form"""
        print(f"Attempting login with username: {username}")
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        # Wait for navigation after login
        self.page.wait_for_load_state('networkidle')

    def verify_login_success(self):
        """Verify successful login"""
        # Check for URL change or presence of main content
        current_url = self.page.url
        print(f"Current URL after login: {current_url}")
        assert "login" not in current_url.lower(), "Still on login page after successful login"

    def verify_login_error(self):
        """Verify error message appears on failed login"""
        self.assert_visible(self.ERROR_MESSAGE)

    def verify_login_failed(self):
        """Verify login attempt failed and login form remains visible."""
        self.page.wait_for_timeout(1000)
        error_locator = self.page.locator(self.ERROR_MESSAGE).first
        if self.page.locator(self.ERROR_MESSAGE).count() > 0:
            assert error_locator.is_visible(), \
                "Expected an error message to be visible after failed login"
        else:
            assert self.page.locator(self.USERNAME_INPUT).count() > 0, \
                "Expected login form to remain visible after failed login"
            assert self.page.locator(self.DASHBOARD_HEADER).count() == 0, \
                "Unexpected dashboard content present after failed login"

    def wait_for_page_load(self, timeout: int = 5000):
        """Wait for page to fully load"""
        self.page.wait_for_load_state('networkidle', timeout=timeout)

    def get_current_url(self) -> str:
        """Get current page URL"""
        return self.page.url
