class PageObjectGenerationSkill:
    def generate_page_object(self, module_name: str, locators: dict) -> str:
        class_name = f"{module_name.capitalize()}Page"

        locator_lines = ""
        for locator_name, locator_value in locators.items():
            locator_lines += f'    {locator_name.upper()} = "{locator_value}"\n'

        return f'''from pages.base_page import BasePage


class {class_name}(BasePage):
{locator_lines}
    def open_page(self, base_url: str):
        self.navigate(base_url)
'''
