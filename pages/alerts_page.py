class AlertsPage:

    def __init__(self, page):
        self.page = page

        self.simple_alert = "#alertBtn"
        self.confirm_alert = "#confirmBtn"
        self.prompt_alert = "#promptBtn"
        self.new_tab = "text=New Tab"
        self.popup_window = "#PopUp"


    def click_simple_alert(self):
        self.page.locator(self.simple_alert).click()


    def click_confirmation_alert(self):
        self.page.locator(self.confirm_alert).click()


    def click_prompt_alert(self):
        self.page.locator(self.prompt_alert).click()


    def click_new_tab(self):
        self.page.locator(self.new_tab).click()


    def click_popup(self):
        self.page.locator(self.popup_window).click()
 