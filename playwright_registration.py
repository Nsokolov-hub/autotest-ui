from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    
    email_input = page.locator("//input[@id=':r0:']")
    username_input = page.locator("//input[@id=':r1:']")
    password_input = page.locator("//input[@id=':r2:']")
    
    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")
    
    registration_button = page.locator("//button[@id='registration-page-registration-button']")
    registration_button.click()
    
    dashboard_element = page.locator("//h6[normalize-space()='Dashboard']")
    expect(dashboard_element).to_have_text("Dashboard")
    
    