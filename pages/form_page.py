class FormPage:

    def __init__(self, page):
        self.page = page

        #locators
        self.section1_input = "(//input[@type='text'])[1]"
        self.section2_input = "(//input[@type='text'])[2]"
        self.section3_input = "(//input[@type='text'])[3]"

        self.section1_submit = "(//button[text()='Submit'])[1]"
        self.section2_submit = "(//button[text()='Submit'])[2]"
        self.section3_submit = "(//button[text()='Submit'])[3]"


    def fill_section1(self, text):
        self.page.locator(self.section1_input).fill(text)

    def fill_section2(self, text):
        self.page.locator(self.section2_input).fill(text)

    def fill_section3(self, text):
        self.page.locator(self.section3_input).fill(text)


    def submit_section1(self):
        self.page.locator(self.section1_submit).click()

    def submit_section2(self):
        self.page.locator(self.section2_submit).click()

    def submit_section3(self):
        self.page.locator(self.section3_submit).click()