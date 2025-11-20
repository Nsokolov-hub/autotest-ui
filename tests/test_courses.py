import pytest
from playwright.sync_api import Page, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page) -> None:
    page = chromium_page_with_state

    page.goto(
        "https://nikita-filonov.github.io/"
        "qa-automation-engineer-ui-course/#/courses"
    )

    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    empty_block_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_block_icon).to_be_visible()

    no_results_block = page.get_by_test_id(
        "courses-list-empty-view-title-text"
    )
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_contain_text("There is no results")

    description_block = page.get_by_test_id(
        "courses-list-empty-view-description-text"
    )
    expect(description_block).to_be_visible()
    expect(
        description_block
    ).to_have_text("Results from the load test pipeline will be displayed here")

