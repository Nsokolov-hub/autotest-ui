import pytest
from playwright.sync_api import Page, expect


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email,password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password"),
    ],
)
def test_wrong_email_or_password_authorization(
    chromium_page: Page, email: str, password: str
) -> None:
    page = chromium_page

    page.goto(
        "https://nikita-filonov.github.io/"
        "qa-automation-engineer-ui-course/#/auth/login"
    )

    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    password_input = page.get_by_test_id("login-form-password-input").locator(
        "input"
    )
    login_button = page.get_by_test_id("login-page-login-button")

    email_input.fill(email)
    password_input.fill(password)
    login_button.click()

    # проверяем появление уведомления об ошибке
    alert = page.get_by_test_id("notification")
    # fallback: иногда уведомление может не иметь data-test-id, ищем по тексту
    if alert.count() == 0:
        alert = page.get_by_text("Wrong email or password")

    expect(alert).to_be_visible()
    expect(alert).to_have_text("Wrong email or password")
