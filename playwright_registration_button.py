from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

   
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    page.get_by_test_id('registration-form-email-input').fill('user.name@gmail.com')
    page.get_by_test_id('registration-form-username-input').fill('username')
    page.get_by_test_id('registration-form-password-input').fill('password')

 
    expect(registration_button).to_be_enabled()

