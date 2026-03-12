from pages.pagination_table_page import PaginationTablePage


def test_select_product(page):

    page.goto(
        "https://testautomationpractice.blogspot.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    table = PaginationTablePage(page)

    result = table.select_product("Tablet")

    assert result

