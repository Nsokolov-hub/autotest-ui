from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            "https://nikita-filonov.github.io/"
            "qa-automation-engineer-ui-course/#/auth/registration"
        )

        registration_button = page.get_by_test_id(
            "registration-page-registration-button"
        )
        expect(registration_button).to_be_disabled()

        email_input = (
            page.get_by_test_id("registration-form-email-input").locator("input")
        )
        email_input.fill("user.name@gmail.com")

        username_input = (
            page.get_by_test_id("registration-form-username-input").locator("input")
        )
        username_input.fill("username")

        password_input = (
            page.get_by_test_id("registration-form-password-input").locator("input")
        )
        password_input.fill("password")

        expect(registration_button).to_be_enabled()
        registration_button.click()

        context.storage_state(path="browser-state.json")
        

        new_browser = playwright.chromium.launch(headless=False)
        new_context = new_browser.new_context(storage_state="browser-state.json")
        new_page = new_context.new_page()

        new_page.goto(
            "https://nikita-filonov.github.io/"
            "qa-automation-engineer-ui-course/#/courses"
        )

        courses_title = new_page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        empty_block_icon = new_page.get_by_test_id("courses-list-empty-view-icon")
        expect(empty_block_icon).to_be_visible()

        no_results_block = new_page.get_by_test_id("courses-list-empty-view-title-text")
        expect(no_results_block).to_be_visible()
        expect(no_results_block).to_contain_text("There is no results")

        description_block = new_page.get_by_test_id(
            "courses-list-empty-view-description-text"
        )
        expect(description_block).to_be_visible()
        expect(
            description_block
        ).to_have_text("Results from the load test pipeline will be displayed here")

        

