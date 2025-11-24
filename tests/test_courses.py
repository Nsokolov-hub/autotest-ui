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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page, courses_list_page) -> None:
    create_course_page.open_create_course_page()

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_course_page.check_visible_create_course_form()
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    import os
    import glob
    import pytest

    # Prefer explicit env var `IMAGE_PATH` if provided
    img_path = os.environ.get("IMAGE_PATH")
    if not img_path or not os.path.isfile(img_path):
        # Fallback: look for an existing image file in `testdata/files/`
        img_dir = os.path.join(os.getcwd(), "testdata", "files")
        pattern = os.path.join(img_dir, "*")
        candidates = [p for p in glob.glob(pattern) if os.path.splitext(p)[1].lower() in (".png", ".jpg", ".jpeg", ".webp")]
        if candidates:
            img_path = candidates[0]
        else:
            pytest.skip("No image found for course. Set IMAGE_PATH or add an image to testdata/files/")

    create_course_page.upload_preview_image(img_path)
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
    )

    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()

    courses_list_page.check_visible_course_card(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )

