class GUIPage:

    def __init__(self, page):
        self.page = page

 
    name_input = "#name"
    email_input = "#email"
    phone_input = "#phone"
    male_radio = "#male"
    sunday_checkbox = "#sunday"
    country_dropdown = "#country"
    color_dropdown = "#colors"
    date_input = "#datepicker"

   
    def enter_name(self, name):
        self.page.fill(self.name_input, name)

    def enter_email(self, email):
        self.page.fill(self.email_input, email)

    def enter_phone(self, phone):
        self.page.fill(self.phone_input, phone)

    def select_gender_male(self):
        self.page.check(self.male_radio)

    def select_sunday(self):
        self.page.check(self.sunday_checkbox)

    def select_country(self, country):
        self.page.select_option(self.country_dropdown, label=country)

    def select_color(self, color):
        self.page.select_option(self.color_dropdown, label=color)

    def select_date(self, date):
        self.page.fill(self.date_input, date)

    def get_name_value(self):
        return self.page.input_value(self.name_input)

    def is_male_selected(self):
        return self.page.is_checked(self.male_radio)

    def is_sunday_selected(self):
        return self.page.is_checked(self.sunday_checkbox)