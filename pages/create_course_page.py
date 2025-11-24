from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')
        self.preview_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')

        self.preview_image_upload_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.preview_image_upload_title = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-title-text'
        )
        self.preview_image_upload_description = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-description-text'
        )
        self.preview_image_upload_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-upload-button'
        )
        self.preview_image_remove_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-remove-button'
        )
        self.preview_image_upload_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')

        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_time_input = (
            page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        )
        self.create_course_description_textarea = (
            page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        )
        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        self.exercises_empty_view_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_empty_view_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.exercises_empty_view_description = page.get_by_test_id(
            'create-course-exercises-empty-view-description-text'
        )

    def check_visible_create_course_title(self) -> None:
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def check_disabled_create_course_button(self) -> None:
        expect(self.create_course_button).to_be_disabled()

    def check_visible_image_preview_empty_view(self) -> None:
        expect(self.preview_empty_view_icon).to_be_visible()
        expect(self.preview_empty_view_title).to_be_visible()
        expect(self.preview_empty_view_description).to_be_visible()

    def check_visible_image_upload_view(self, is_image_uploaded: bool = False) -> None:
        if is_image_uploaded:
            expect(self.preview_image).to_be_visible()
            expect(self.preview_image_remove_button).to_be_visible()
        else:
            expect(self.preview_image_upload_icon).to_be_visible()
            expect(self.preview_image_upload_title).to_be_visible()
            expect(self.preview_image_upload_description).to_be_visible()
            expect(self.preview_image_upload_button).to_be_visible()

    def upload_preview_image(self, path: str) -> None:
        self.preview_image_upload_input.set_input_files(path)

    def check_visible_create_course_form(self) -> None:
        expect(self.create_course_title_input).to_be_visible()
        expect(self.create_course_title_input).to_have_value("")
        expect(self.create_course_estimated_time_input).to_be_visible()
        expect(self.create_course_estimated_time_input).to_have_value("")
        expect(self.create_course_description_textarea).to_be_visible()
        
        expect(self.create_course_max_score_input).to_have_value("0")
        expect(self.create_course_min_score_input).to_have_value("0")

    def fill_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str) -> None:
        self.create_course_title_input.fill(title)
        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_description_textarea.fill(description)
        self.create_course_max_score_input.fill(max_score)
        self.create_course_min_score_input.fill(min_score)

    def click_create_course_button(self) -> None:
        self.create_course_button.click()
        try:
            self.page.wait_for_url("**#/courses", timeout=5000)
        except Exception:
            from playwright.sync_api import expect as _expect

            _expect(self.page.get_by_test_id('courses-list-toolbar-title-text')).to_be_visible()

    def open_create_course_page(self) -> None:
        self.page.goto(
            "https://nikita-filonov.github.io/"
            "qa-automation-engineer-ui-course/#/courses/create"
        )

    def check_visible_exercises_title(self) -> None:
        expect(self.exercises_title).to_be_visible()

    def check_visible_create_exercise_button(self) -> None:
        expect(self.create_exercise_button).to_be_visible()

    def check_visible_exercises_empty_view(self) -> None:
        expect(self.exercises_empty_view_icon).to_be_visible()
        expect(self.exercises_empty_view_title).to_be_visible()
        expect(self.exercises_empty_view_description).to_be_visible()
