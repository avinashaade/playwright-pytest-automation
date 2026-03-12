class CheckboxPage:

    def __init__(self, page):
        self.page = page

        self.sunday_checkbox = "#sunday"
        self.monday_checkbox = "#monday"
        self.tuesday_checkbox = "#tuesday"

    def check_sunday(self):
        self.page.locator(self.sunday_checkbox).check()

    def check_monday(self):
        self.page.locator(self.monday_checkbox).check()

    def check_tuesday(self):
        self.page.locator(self.tuesday_checkbox).check()