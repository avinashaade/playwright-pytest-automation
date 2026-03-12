from pages.hover_page import HoverPage

def test_mouse_hover(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    hover = HoverPage(page)

    hover.hover_over_button()

    hover.click_mobile_option()