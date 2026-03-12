class LinksPage:

    def __init__(self, page):
        self.page = page
        self.apple_link = page.locator("#apple")
        self.lenovo_link = page.locator("#lenovo")
        self.dell_link = page.locator("#dell")

    def click_apple(self):
        self.apple_link.click()

    def click_lenovo(self):
        self.lenovo_link.click()

    def click_dell(self):
        self.dell_link.click()