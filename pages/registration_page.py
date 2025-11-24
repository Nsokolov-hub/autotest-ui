from playwright.sync_api import Page, expect


BASE_URL = (
    "https://nikita-filonov.github.io/"
    "qa-automation-engineer-ui-course/#"
)


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.registration_button = page.get_by_test_id("registration-page-registration-button")
        self.email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        self.username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        self.password_input = page.get_by_test_id("registration-form-password-input").locator("input")

    def open_registration_page(self) -> None:
        self.page.goto(f"{BASE_URL}/auth/registration")

    def fill_registration_form(self, email: str, username: str, password: str) -> None:
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_registration_button(self) -> None:
        self.registration_button.click()
