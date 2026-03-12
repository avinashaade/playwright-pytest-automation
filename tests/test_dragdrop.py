from pages.dragdrop_page import DragDropPage


def test_drag_drop(page):
    dd = DragDropPage(page)

    dd.drag_drop()

    assert "Dropped" in dd.get_drop_result_text()