import time
import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage) -> None:
    # generate a unique email to avoid conflicts
    unique = str(int(time.time()))
    email = f"test.user+{unique}@example.com"
    username = f"testuser{unique}"
    password = "password"

    registration_page.open_registration_page()
    registration_page.fill_registration_form(email, username, password)
    registration_page.click_registration_button()

    # after successful registration user should land on Dashboard
    dashboard_page.expect_dashboard_title_visible()
