from pages.table_page import TablePage

def test_table(page):
    table = TablePage(page)

    assert table.row_count() > 0