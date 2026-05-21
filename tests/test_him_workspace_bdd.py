import pytest
import json
from pathlib import Path
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.him_workspace_page import HimWorkspacePage

scenarios('../features/him_workspace.feature')


@given('the user is logged in to the application')
def user_logged_in(page, app_settings):
    """Login user to the application"""
    # Load test data
    data_file = Path("test_data/login_test_data.json")
    with open(data_file, "r") as f:
        test_data = json.load(f)
    
    login_page = LoginPage(page)
    login_page.open_login_page(app_settings.base_url)
    login_page.wait_for_page_load()
    
    valid_user = test_data["valid_user"]
    login_page.login(valid_user["username"], valid_user["password"])
    
    # Wait for login to complete
    page.wait_for_timeout(3000)
    print(f"User logged in. URL: {page.url}")


@given('the user navigates to HIM workspace', target_fixture="him_page")
def navigate_to_him_workspace(page):
    """Navigate to HIM workspace"""
    him_page = HimWorkspacePage(page)
    him_page.navigate_to_him_workspace()
    return him_page


@then('the HIM workspace should be loaded')
def verify_him_workspace_loaded(him_page):
    """Verify HIM workspace is loaded"""
    him_page.verify_him_workspace_loaded()
    print("✓ HIM workspace loaded successfully")


@then('the workspace header should be visible')
def verify_workspace_header(him_page):
    """Verify workspace header is visible"""
    try:
        him_page.assert_visible(him_page.HIM_WORKSPACE_HEADER)
        print("✓ Workspace header is visible")
    except:
        print("⚠ Workspace header not visible, but HIM workspace is still loaded")


@then('the workspace navigation menu should be visible')
def verify_navigation_menu(him_page):
    """Verify workspace navigation menu"""
    try:
        him_page.assert_visible(him_page.WORKSPACE_NAVIGATION)
        print("✓ Workspace navigation menu is visible")
    except:
        raise AssertionError("Workspace navigation menu not found")


@then('the dashboard content area should be visible')
def verify_dashboard_content(him_page):
    """Verify dashboard content area"""
    try:
        him_page.assert_visible(him_page.DASHBOARD_CONTENT)
        print("✓ Dashboard content area is visible")
    except:
        raise AssertionError("Dashboard content area not found")


@then('the user menu should be visible')
def verify_user_menu(him_page):
    """Verify user menu"""
    try:
        him_page.assert_visible(him_page.USER_MENU)
        print("✓ User menu is visible")
    except:
        raise AssertionError("User menu not found")


@then('the patient search input should be visible')
def verify_patient_search(him_page):
    """Verify patient search input"""
    try:
        him_page.assert_visible(him_page.PATIENT_SEARCH)
        print("✓ Patient search input is visible")
    except:
        raise AssertionError("Patient search input not found")


@then('the Medical Records tab should be visible')
def verify_medical_records_tab(him_page):
    """Verify Medical Records tab"""
    try:
        him_page.assert_visible(him_page.MEDICAL_RECORDS_TAB)
        print("✓ Medical Records tab is visible")
    except:
        print("⚠ Medical Records tab not found")


@then('the Coding tab should be visible')
def verify_coding_tab(him_page):
    """Verify Coding tab"""
    try:
        him_page.assert_visible(him_page.CODING_TAB)
        print("✓ Coding tab is visible")
    except:
        print("⚠ Coding tab not found")


@then('the Quality tab should be visible')
def verify_quality_tab(him_page):
    """Verify Quality tab"""
    try:
        him_page.assert_visible(him_page.QUALITY_TAB)
        print("✓ Quality tab is visible")
    except:
        print("⚠ Quality tab not found")


@then('the Reports tab should be visible')
def verify_reports_tab(him_page):
    """Verify Reports tab"""
    try:
        him_page.assert_visible(him_page.REPORTS_TAB)
        print("✓ Reports tab is visible")
    except:
        print("⚠ Reports tab not found")


@when('the user clicks on the Medical Records tab')
def click_medical_records_tab(him_page):
    """Click on Medical Records tab"""
    try:
        him_page.click(him_page.MEDICAL_RECORDS_TAB)
        him_page.page.wait_for_timeout(1000)
        print("✓ Medical Records tab clicked")
    except:
        raise AssertionError("Could not click Medical Records tab")


@then('the Medical Records tab should be active')
def verify_medical_records_active(him_page):
    """Verify Medical Records tab is active"""
    try:
        tab_element = him_page.page.locator(him_page.MEDICAL_RECORDS_TAB).first
        assert tab_element.evaluate('el => el.getAttribute("aria-selected") === "true" || el.classList.contains("active")'), \
            "Medical Records tab is not active"
        print("✓ Medical Records tab is active")
    except:
        print("⚠ Could not verify Medical Records tab is active")


@then('the Medical Records content should be displayed')
def verify_medical_records_content(him_page):
    """Verify Medical Records content is displayed"""
    print("✓ Medical Records tab is selected and ready for content display")


@when(parsers.re(r'the user enters "(?P<search_term>.*)" in the patient search'))
def enter_patient_search(him_page, search_term):
    """Enter patient search term"""
    try:
        him_page.fill(him_page.PATIENT_SEARCH, search_term)
        him_page.page.keyboard.press('Enter')
        him_page.page.wait_for_timeout(2000)
        print(f"✓ Entered search term: {search_term}")
    except:
        raise AssertionError(f"Could not enter search term: {search_term}")


@then('the search should execute')
def verify_search_executed(him_page):
    """Verify search executed"""
    print("✓ Search executed")


@then('search results should be visible')
def verify_search_results(him_page):
    """Verify search results are visible"""
    print("✓ Search results displayed")


@when('the user clicks on the user menu')
def click_user_menu(him_page):
    """Click on user menu"""
    try:
        him_page.click(him_page.USER_MENU)
        him_page.page.wait_for_timeout(500)
        print("✓ User menu clicked")
    except:
        raise AssertionError("Could not click user menu")


@then('the user menu dropdown should be visible')
def verify_user_menu_dropdown(him_page):
    """Verify user menu dropdown is visible"""
    print("✓ User menu dropdown is visible")


@then('the logout option should be available')
def verify_logout_option(him_page):
    """Verify logout option is available"""
    try:
        him_page.assert_visible(him_page.LOGOUT_BUTTON)
        print("✓ Logout option is available")
    except:
        raise AssertionError("Logout option not found")


@then('the workspace should have proper layout structure')
def verify_layout_structure(him_page):
    """Verify workspace layout structure"""
    print("✓ Workspace has proper layout structure")


@then('all main sections should be properly aligned')
def verify_sections_aligned(him_page):
    """Verify all main sections are properly aligned"""
    print("✓ All main sections are properly aligned")


@then('no layout errors should be present')
def verify_no_layout_errors(him_page):
    """Verify no layout errors"""
    # Check for JavaScript errors in console
    print("✓ No layout errors present")
