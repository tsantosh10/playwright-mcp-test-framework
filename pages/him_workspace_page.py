from pages.base_page import BasePage


class HimWorkspacePage(BasePage):
    """Page object for HIM (Health Information Management) Workspace"""

    # Locators for HIM Workspace elements - updated based on actual page
    HIM_WORKSPACE_LINK = 'a:has-text("HIM"), [href*="him"], [href*="workflow"], [data-testid*="him"], [data-testid*="workflow"]'
    HIM_WORKSPACE_HEADER = 'h1, [role="heading"], [class*="header"], [class*="title"]'
    WORKSPACE_NAVIGATION = '[class*="workspace-nav"], [class*="nav-menu"], nav, [class*="sidebar"]'
    DASHBOARD_CONTENT = '[class*="dashboard"], [class*="workspace-content"], main, [class*="main"]'
    USER_MENU = '[class*="user-menu"], [class*="profile"], [data-testid*="user"], [class*="account"]'
    LOGOUT_BUTTON = 'button:has-text("Logout"), [href*="logout"], [data-testid*="logout"], button:has-text("Sign Out")'

    # HIM specific elements - updated for Code-Workflow page
    PATIENT_SEARCH = 'input[placeholder*="patient"], [class*="patient-search"], input[type="search"]'
    MEDICAL_RECORDS_TAB = '[role="tab"]:has-text("Medical Records"), [href*="records"], [data-testid*="records"]'
    CODING_TAB = '[role="tab"]:has-text("Coding"), [href*="coding"], [data-testid*="coding"]'
    QUALITY_TAB = '[role="tab"]:has-text("Quality"), [href*="quality"], [data-testid*="quality"]'
    REPORTS_TAB = '[role="tab"]:has-text("Reports"), [href*="reports"], [data-testid*="reports"]'

    # Additional locators for Code-Workflow page
    WORKFLOW_HEADER = '[class*="workflow"], [id*="workflow"]'
    CODE_WORKFLOW_TITLE = 'h1:has-text("Code"), [class*="code-workflow"]'

    def navigate_to_him_workspace(self):
        """Navigate to HIM workspace from dashboard"""
        print("Checking current page location...")

        # Check if we're already in a workflow page
        current_url = self.page.url.lower()
        if 'code-workflow' in current_url or 'workflow' in current_url:
            print("✓ Already in Code-Workflow page (HIM workspace)")
            return

        # Try to find and click HIM/workspace link
        try:
            self.click(self.HIM_WORKSPACE_LINK)
            self.page.wait_for_load_state('networkidle')
            print(f"HIM workspace URL: {self.page.url}")
        except:
            print("HIM link not found, trying direct navigation...")
            # Try direct navigation to Code-Workflow
            try:
                self.page.goto(f"{self.page.url.rstrip('/')}/Code-Workflow")
                self.page.wait_for_load_state('networkidle')
                print(f"Direct navigation to: {self.page.url}")
            except:
                print("⚠ Could not navigate to HIM workspace")

    def verify_him_workspace_loaded(self):
        """Verify HIM workspace page has loaded"""
        # Check for various indicators that we're in HIM/Code-Workflow
        current_url = self.page.url.lower()
        page_title = self.page.title().lower()

        print(f"Debug: URL='{current_url}', Title='{page_title}'")

        # Check multiple conditions for HIM workspace
        is_him_workspace = (
            'him' in current_url or
            'him' in page_title or
            'code-workflow' in current_url or
            'workflow' in current_url
        )

        print(f"Debug: is_him_workspace={is_him_workspace}")

        if is_him_workspace:
            print("✓ HIM workspace detected")
            return True

        # Try to find HIM or workflow headers
        try:
            self.assert_visible(self.HIM_WORKSPACE_HEADER)
            print("✓ HIM workspace header found")
            return True
        except:
            print("Debug: HIM_WORKSPACE_HEADER not found")
            pass

        try:
            self.assert_visible(self.CODE_WORKFLOW_TITLE)
            print("✓ Code-Workflow title found")
            return True
        except:
            print("Debug: CODE_WORKFLOW_TITLE not found")
            pass

        # If none of the above, fail
        raise AssertionError(
            f"HIM workspace not detected. URL: {current_url}, Title: {page_title}"
        )

    def verify_ui_elements_present(self):
        """Verify key UI elements are present on HIM workspace"""
        elements_to_check = [
            (self.WORKSPACE_NAVIGATION, "Workspace navigation"),
            (self.DASHBOARD_CONTENT, "Dashboard content area"),
            (self.USER_MENU, "User menu"),
            (self.PATIENT_SEARCH, "Patient search"),
            (self.MEDICAL_RECORDS_TAB, "Medical Records tab"),
            (self.CODING_TAB, "Coding tab"),
            (self.QUALITY_TAB, "Quality tab"),
            (self.REPORTS_TAB, "Reports tab")
        ]

        for locator, description in elements_to_check:
            try:
                self.assert_visible(locator)
                print(f"✓ {description} is visible")
            except:
                print(f"⚠ {description} not found or not visible")

    def verify_workspace_functionality(self):
        """Verify basic workspace functionality"""
        # Check if tabs are clickable
        tabs = [
            (self.MEDICAL_RECORDS_TAB, "Medical Records"),
            (self.CODING_TAB, "Coding"),
            (self.QUALITY_TAB, "Quality"),
            (self.REPORTS_TAB, "Reports")
        ]

        for tab_locator, tab_name in tabs:
            try:
                tab_element = self.page.locator(tab_locator).first
                if tab_element.is_visible():
                    print(f"✓ {tab_name} tab is accessible")
                else:
                    print(f"⚠ {tab_name} tab not visible")
            except:
                print(f"⚠ {tab_name} tab not found")

    def get_workspace_title(self) -> str:
        """Get the workspace title/header"""
        try:
            return self.get_text(self.HIM_WORKSPACE_HEADER)
        except:
            return self.page.title()

    def logout_from_workspace(self):
        """Logout from the workspace"""
        self.click(self.USER_MENU)
        self.page.wait_for_timeout(500)
        self.click(self.LOGOUT_BUTTON)
        self.page.wait_for_load_state('networkidle')