class HoverPage:

    def __init__(self, page):
        self.page = page
        self.hover_button = page.locator("button:has-text('Point Me')")
        self.mobile_option = page.get_by_role("link", name="Mobiles")

    def hover_over_button(self):
        self.hover_button.hover() 
    def click_mobile_option(self):
        self.mobile_option.click()