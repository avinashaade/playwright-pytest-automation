class DynamicButtonPage:

    def __init__(self, page):
        self.page = page
        self.start_button = page.locator("button:has-text('START')")
        self.stop_button = page.locator("button:has-text('STOP')")

    def click_start(self):
        self.start_button.click()

    def click_stop(self):
        self.stop_button.wait_for()
        self.stop_button.click()