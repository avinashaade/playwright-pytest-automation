class DatePickerPage:

    def __init__(self, page):
        self.page = page
        self.date_input = "#datepicker"

    def enter_date(self, date):
        self.page.fill(self.date_input, date)

    def get_date(self):
        return self.page.input_value(self.date_input)