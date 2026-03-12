from pages.dynamic_button_page import DynamicButtonPage

def test_dynamic_button(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    button = DynamicButtonPage(page)

    button.click_start()

    button.click_stop()