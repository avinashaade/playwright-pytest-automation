class TablePage:

    def __init__(self, page):
        self.page = page

    def row_count(self):
        return self.page.locator("table[name='BookTable'] tr").count()