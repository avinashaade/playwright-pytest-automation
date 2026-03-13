from pages.window_page import WindowPage


def test_new_window(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    window = WindowPage(page)

    new_page = window.open_new_tab()

    assert new_page.url != ""