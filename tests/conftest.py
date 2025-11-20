import pytest
from pathlib import Path

from playwright.sync_api import Playwright, Page, expect, sync_playwright


BASE_URL = (
    "https://nikita-filonov.github.io/"
    "qa-automation-engineer-ui-course/#"
)

BROWSER_STATE_PATH = Path("browser-state.json")


@pytest.fixture(scope="session")
def playwright() -> Playwright:
    
    playwright_instance = sync_playwright().start()
    yield playwright_instance
    playwright_instance.stop()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(f"{BASE_URL}/auth/registration")

    registration_button = page.get_by_test_id(
        "registration-page-registration-button"
    )
    expect(registration_button).to_be_disabled()

    email_input = page.get_by_test_id(
        "registration-form-email-input"
    ).locator("input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id(
        "registration-form-username-input"
    ).locator("input")
    username_input.fill("username")

    password_input = page.get_by_test_id(
        "registration-form-password-input"
    ).locator("input")
    password_input.fill("password")

    expect(registration_button).to_be_enabled()
    registration_button.click()

    context.storage_state(path=str(BROWSER_STATE_PATH))
    
    


@pytest.fixture(scope="function")
def chromium_page_with_state(
    initialize_browser_state, playwright: Playwright
) -> Page:
    

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=str(BROWSER_STATE_PATH))
    page = context.new_page()

    yield page

    


