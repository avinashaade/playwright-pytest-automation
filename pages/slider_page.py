class SliderPage:

    def __init__(self, page):
        self.page = page

        # choose first slider handle
        self.slider = ".ui-slider-handle"
        self.price = "#amount"

    def move_slider_right(self):

        slider = self.page.locator(self.slider).first

        box = slider.bounding_box()

        self.page.mouse.move(
            box["x"] + box["width"]/2,
            box["y"] + box["height"]/2
        )

        self.page.mouse.down()

        self.page.mouse.move(box["x"] + 150, box["y"])

        self.page.mouse.up()

    def get_price_range(self):

        return self.page.locator(self.price).input_value()
    

