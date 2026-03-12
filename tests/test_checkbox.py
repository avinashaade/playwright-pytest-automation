from pages.checkbox_page import CheckboxPage


def test_select_single_checkbox(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    checkbox = CheckboxPage(page)

    checkbox.check_sunday()

    assert page.locator("#sunday").is_checked()


def test_select_multiple_checkboxes(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    checkbox = CheckboxPage(page)

    checkbox.check_sunday()
    checkbox.check_monday()
    checkbox.check_tuesday()

    assert page.locator("#sunday").is_checked()
    assert page.locator("#monday").is_checked()
    assert page.locator("#tuesday").is_checked()