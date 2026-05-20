# iMedx Login Test Suite - Quick Reference

## Test Suite Overview
This test suite validates login functionality for the iMedx application at:
**https://san-hcs-dev.imedx.com.au/**

### Test Credentials
- **Username:** Sai
- **Password:** Imedx@123

---

## Running Tests

### Run All Tests
```bash
cd "c:\PlayWright\playwright-mcp-test-framework (1)\playwright-mcp-test-framework"
.venv\Scripts\activate
pytest tests/test_imedx_login_optimized.py -v
```

### Run with HTML Report
```bash
pytest tests/test_imedx_login_optimized.py -v --html=reports/imedx_report.html --self-contained-html
```

### Run Specific Test
```bash
pytest tests/test_imedx_login_optimized.py::TestImedxLoginOptimized::test_01_valid_login_with_valid_credentials -v
```

### Run with Detailed Output
```bash
pytest tests/test_imedx_login_optimized.py -v -s
```

---

## Test Suite (10 Tests)

| # | Test | Description | Status |
|---|------|-------------|--------|
| 1 | test_01_valid_login_with_valid_credentials | Primary test - Login with Sai / Imedx@123 | ✅ PASSED |
| 2 | test_02_page_loads_correctly | Verify login page loads | ✅ PASSED |
| 3 | test_03_username_input_field_exists | Username field is present and visible | ✅ PASSED |
| 4 | test_04_password_input_field_exists | Password field is present and masked | ✅ PASSED |
| 5 | test_05_login_button_exists | Login button is present and visible | ✅ PASSED |
| 6 | test_06_can_enter_username_text | Username field accepts input | ✅ PASSED |
| 7 | test_07_can_enter_password_text | Password field accepts input | ✅ PASSED |
| 8 | test_08_login_form_submission | Form submission with valid credentials | ✅ PASSED |
| 9 | test_09_session_established_after_login | Session verification after login | ✅ PASSED |
| 10 | test_10_credentials_data_loaded_correctly | Test data validation | ✅ PASSED |

---

## Test Files

### Primary Files
- **tests/test_imedx_login_optimized.py** - Main test suite (10 tests) ⭐ RECOMMENDED
- **tests/test_imedx_login.py** - Original test suite (8 tests)
- **pages/login_page.py** - Login page object model
- **config/environments.yaml** - URL and environment settings
- **test_data/login_test_data.json** - Test credentials and data

---

## Configuration Files Updated

### environments.yaml
```yaml
dev:
  base_url: "https://san-hcs-dev.imedx.com.au"
  browser: "chromium"
  headless: false

qa:
  base_url: "https://san-hcs-dev.imedx.com.au"
  browser: "chromium"
  headless: true
```

### login_test_data.json
```json
{
  "valid_user": {
    "username": "Sai",
    "password": "Imedx@123"
  },
  "invalid_user": {
    "username": "wrong_user",
    "password": "wrong_password"
  },
  "empty_credentials": {
    "username": "",
    "password": ""
  }
}
```

---

## Test Reports

HTML reports are generated in the `reports/` directory:
- `imedx_optimized_report.html` - Latest optimized test run
- `imedx_login_report.html` - Original test run
- `report.html` - Default report

Open any HTML report in a browser to view detailed test results with screenshots.

---

## Framework Architecture

```
Test Script
    ↓
LoginPage (Page Object Model)
    ↓
BasePage (Common base functionality)
    ↓
Playwright Browser
    ↓
iMedx Application (https://san-hcs-dev.imedx.com.au/)
```

### Key Classes

**LoginPage** - Page Object for login functionality
- `open_login_page()` - Navigate to login page
- `login(username, password)` - Perform login
- `verify_login_success()` - Verify successful login
- `get_current_url()` - Get current page URL
- `wait_for_page_load()` - Wait for page to load

**BasePage** - Common page functionality
- `navigate(url)` - Navigate to URL
- `fill(locator, value)` - Fill input field
- `click(locator)` - Click element
- `assert_visible(locator)` - Assert element is visible

---

## Test Execution Results

**Total Tests:** 10  
**Passed:** 10 ✅  
**Failed:** 0  
**Execution Time:** ~57 seconds  
**Browser:** Chromium  

---

## Notes

- Tests use Playwright for browser automation
- Page Object Model (POM) pattern for maintainability
- Pytest framework for test execution
- Chrome Headless Shell for CI/CD environments
- HTML reports with screenshots (when failures occur)

---

## Troubleshooting

### Issue: Tests timeout
**Solution:** Increase timeout in `wait_for_page_load()` or update network conditions

### Issue: Locators not found
**Solution:** The dynamic selectors in `LoginPage` should handle most UI variations. If needed, inspect the page and update locators.

### Issue: Browser not starting
**Solution:** Run `playwright install` to download browser binaries

---

## Next Steps

1. **CI/CD Integration** - Add to your CI/CD pipeline
2. **Parallel Execution** - Run tests in parallel with pytest-xdist
3. **Cross-browser Testing** - Add Firefox and WebKit tests
4. **Extended Coverage** - Add tests for other pages/features
5. **Performance Testing** - Add page load time assertions
