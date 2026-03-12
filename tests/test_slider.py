from pages.slider_page import SliderPage


def test_slider_move(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    slider = SliderPage(page)

    page.locator("text=Slider").scroll_into_view_if_needed()

    slider.move_slider_right()

    price = slider.get_price_range()

    print(price)

    assert price is not None