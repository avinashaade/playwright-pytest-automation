from pages.form_page import FormPage


def test_form_submission(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    form = FormPage(page)

    form.fill_section1("Automation Test 1")
    form.submit_section1()

    form.fill_section2("Automation Test 2")
    form.submit_section2()

    form.fill_section3("Automation Test 3")
    form.submit_section3()