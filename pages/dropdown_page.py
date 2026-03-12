class DropdownPage:

    def __init__(self, page):
        self.page = page

        self.dropdown = "#comboBox"
        self.options = "#comboBox option"

    def select_item(self, item_name):

        self.page.locator(self.dropdown).click()

        self.page.locator(f"text={item_name}").scroll_into_view_if_needed()

        self.page.locator(f"text={item_name}").click()