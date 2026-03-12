from pages.dropdown_page import DropdownPage


def test_scroll_dropdown(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    dropdown = DropdownPage(page)

    page.locator("text=Scrolling DropDown").scroll_into_view_if_needed()

    dropdown.select_item("Item 95")

    selected = page.locator("#comboBox").input_value()

    print(selected)

    assert selected == "Item 95"