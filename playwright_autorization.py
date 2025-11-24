from playwright.sync_api import Page, expect

from playwright.sync_api import sync_playwright, expect  


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    page.get_by_role()