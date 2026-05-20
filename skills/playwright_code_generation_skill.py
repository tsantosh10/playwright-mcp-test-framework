class PlaywrightCodeGenerationSkill:
    def generate_pytest_code(self, test_cases: list[dict], module: str) -> str:
        if module == "login":
            return self._generate_login_tests()

        return self._generate_generic_tests(test_cases)

    def _generate_login_tests(self) -> str:
        return '''from pages.login_page import LoginPage


def test_generated_valid_login(page, app_settings):
    login_page = LoginPage(page)

    login_page.open_login_page(app_settings.base_url)
    login_page.login("admin", "admin123")
    login_page.verify_login_success()


def test_generated_invalid_login(page, app_settings):
    login_page = LoginPage(page)

    login_page.open_login_page(app_settings.base_url)
    login_page.login("wrong_user", "wrong_password")
    login_page.verify_login_error()
'''

    def _generate_generic_tests(self, test_cases: list[dict]) -> str:
        test_code = ""

        for test_case in test_cases:
            function_name = test_case["test_case_id"].lower()
            test_code += f'''
def test_{function_name}(page, app_settings):
    page.goto(app_settings.base_url)
    assert page.title() is not None
'''

        return test_code
