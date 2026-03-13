from pages.datepicker_page import DatePickerPage


def test_select_date(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    datepicker = DatePickerPage(page)

    datepicker.enter_date("03/25/2026")

    selected_date = datepicker.get_date()

    assert selected_date == "03/25/2026"