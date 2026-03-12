class DragDropPage:
    """
    Page Object: Drag and Drop Section
    Scenario: Verify user can drag item and drop into target area.
    """

    def __init__(self, page):
        self.page = page

    # Locators
    draggable = "#draggable"
    droppable = "#droppable"

    # Actions
    def drag_drop(self):
        self.page.drag_and_drop(self.draggable, self.droppable)

    # Assertions helper
    def get_drop_result_text(self):
        return self.page.inner_text(self.droppable)