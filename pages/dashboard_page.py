from playwright.sync_api import Page, expect


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")

    def expect_dashboard_title_visible(self) -> None:
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text("Dashboard")
