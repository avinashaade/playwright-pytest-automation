from pages.alerts_page import AlertsPage


def test_simple_alert(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    alert = AlertsPage(page)

    page.on("dialog", lambda dialog: dialog.accept())

    alert.click_simple_alert()



def test_confirmation_alert(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    alert = AlertsPage(page)

    page.on("dialog", lambda dialog: dialog.accept())

    alert.click_confirmation_alert()



def test_prompt_alert(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    alert = AlertsPage(page)

    page.on("dialog", lambda dialog: dialog.accept("Playwright Test"))

    alert.click_prompt_alert()



def test_new_tab(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    alert = AlertsPage(page)

    with page.context.expect_page() as new_page:

        alert.click_new_tab()

    tab = new_page.value

    print(tab.title())



def test_popup_window(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    alert = AlertsPage(page)

    with page.context.expect_page() as popup:

        alert.click_popup()

    popup_page = popup.value

    print(popup_page.title())