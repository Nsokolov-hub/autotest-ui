import pytest
from playwright.sync_api import Page

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    """Return a RegistrationPage instance bound to the project's Page fixture."""
    return RegistrationPage(chromium_page)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    """Return a DashboardPage instance bound to the project's Page fixture."""
    return DashboardPage(chromium_page)


@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    """Return a CreateCoursePage instance bound to an authenticated Page fixture."""
    return CreateCoursePage(chromium_page_with_state)


@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    """Return a CoursesListPage instance bound to an authenticated Page fixture."""
    return CoursesListPage(chromium_page_with_state)
