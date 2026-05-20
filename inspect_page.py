import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from config.settings import Settings
import json

# Load settings
settings = Settings()
with open('test_data/login_test_data.json', 'r') as f:
    test_data = json.load(f)

def inspect_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login
        login_page = LoginPage(page)
        login_page.open_login_page(settings.base_url)
        login_page.wait_for_page_load()

        valid_user = test_data['valid_user']
        login_page.login(valid_user['username'], valid_user['password'])
        page.wait_for_timeout(5000)

        print('=== PAGE INSPECTION AFTER LOGIN ===')
        print('URL:', page.url)
        print('Title:', page.title())

        # Get all links
        links = page.query_selector_all('a')
        print(f'\nFound {len(links)} links:')
        for i, link in enumerate(links[:20]):  # First 20 links
            text = link.inner_text().strip()
            href = link.get_attribute('href') or ''
            if text or href:
                print(f'{i+1}. "{text}" -> {href}')

        # Get all buttons
        buttons = page.query_selector_all('button')
        print(f'\nFound {len(buttons)} buttons:')
        for i, button in enumerate(buttons[:15]):  # First 15 buttons
            text = button.inner_text().strip()
            if text:
                print(f'{i+1}. Button: "{text}"')

        # Look for navigation menus
        nav_elements = page.query_selector_all('nav, [class*="nav"], [class*="menu"]')
        print(f'\nFound {len(nav_elements)} navigation elements')

        # Look for any element containing "HIM", "workflow", "code"
        him_elements = page.query_selector_all('[class*="him"], [class*="workflow"], [class*="code"], [id*="him"], [id*="workflow"], [id*="code"]')
        print(f'\nFound {len(him_elements)} elements with him/workflow/code classes/ids:')

        for elem in him_elements[:10]:
            tag = elem.evaluate('el => el.tagName')
            classes = elem.get_attribute('class') or ''
            id_attr = elem.get_attribute('id') or ''
            text = elem.inner_text().strip()[:50]
            print(f'  {tag}#{id_attr}.{classes}: "{text}"')

        # Look for menu items, sidebar, navigation
        menu_items = page.query_selector_all('[class*="menu"], [class*="sidebar"], [role="menu"], [role="navigation"]')
        print(f'\nFound {len(menu_items)} menu/sidebar elements')

        # Look for any text containing HIM, workflow, medical, etc.
        all_text_elements = page.query_selector_all('*')
        relevant_texts = []
        for elem in all_text_elements:
            text = elem.inner_text().strip().lower()
            if any(keyword in text for keyword in ['him', 'workflow', 'code', 'medical', 'record', 'coding', 'quality', 'report']):
                if len(text) > 3:  # Avoid very short matches
                    relevant_texts.append(text)

        print(f'\nRelevant text content ({len(set(relevant_texts))} unique):')
        for text in sorted(set(relevant_texts))[:15]:
            print(f'  "{text}"')

        # Check for iframes or embedded content
        iframes = page.query_selector_all('iframe')
        print(f'\nFound {len(iframes)} iframes')

        # Try to find any link that might go to an application page
        app_links = []
        for link in links:
            href = link.get_attribute('href') or ''
            if href.startswith('/') and not href.endswith('.mp4') and href != '/admin':
                app_links.append((link, href))

        print(f'\nPotential application links ({len(app_links)}):')
        for link, href in app_links:
            text = link.inner_text().strip()
            print(f'  "{text}" -> {href}')

        # Check page source for any hidden navigation
        page_source = page.content()
        if 'workflow' in page_source.lower():
            print('\n✓ "workflow" found in page source')
        if 'him' in page_source.lower():
            print('✓ "him" found in page source')
        if 'code' in page_source.lower():
            print('✓ "code" found in page source')

        browser.close()

if __name__ == "__main__":
    inspect_page()