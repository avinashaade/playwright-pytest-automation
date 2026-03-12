from pages.links_page import LinksPage

def test_laptop_links(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    link = LinksPage(page)

    link.click_apple()

    assert "apple" in page.url


def test_lenovo_link(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    link = LinksPage(page)

    link.click_lenovo()

    assert "lenovo" in page.url


def test_dell_link(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    link = LinksPage(page)

    link.click_dell()

    assert "dell" in page.url