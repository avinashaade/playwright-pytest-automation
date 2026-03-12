class PaginationTablePage:

    def __init__(self, page):
        self.page = page

        
        self.table_rows = "//table[@id='productTable']/tbody/tr"
        self.pagination_links = "//ul[@class='pagination']//li/a"

    def select_product(self, product_name):

       
        pages = self.page.locator(self.pagination_links).count()

        for p in range(1, pages + 1):

            rows = self.page.locator(self.table_rows).count()

            for r in range(1, rows + 1):

                name = self.page.locator(
                    f"//table[@id='productTable']/tbody/tr[{r}]/td[2]"
                ).text_content().strip()

                if name == product_name:

                    
                    self.page.locator(
                        f"//table[@id='productTable']/tbody/tr[{r}]/td[4]//input"
                    ).check()

                    return True

            
            if p < pages:
                self.page.locator(f"//ul[@class='pagination']//li[{p+1}]").click()

        return False