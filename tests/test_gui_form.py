from pages.gui_page import GUIPage

def test_gui_form(page):
    gui = GUIPage(page)

    gui.enter_name("Avinash")
    gui.enter_email("avinash@test.com")
    gui.enter_phone("9999999999")
    gui.select_gender_male()
    gui.select_sunday()
    gui.select_country("India")
    gui.select_color("Red")
    gui.select_date("03/20/2026")


    assert gui.get_name_value() == "Avinash"
    assert gui.is_male_selected()
    assert gui.is_sunday_selected()