import pytest
from playwright.sync_api import Page

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    """Return a RegistrationPage instance bound to the project's Page fixture."""
    return RegistrationPage(chromium_page)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    """Return a DashboardPage instance bound to the project's Page fixture."""
    return DashboardPage(chromium_page)
