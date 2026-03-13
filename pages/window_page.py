class WindowPage:

    def __init__(self, page):
        self.page = page
        self.external_link = "a[href*='wikipedia']"

    def open_new_tab(self):
        with self.page.expect_popup() as popup:
            self.page.locator(self.external_link).first.click()

        new_page = popup.value
        new_page.wait_for_load_state()

        return new_page