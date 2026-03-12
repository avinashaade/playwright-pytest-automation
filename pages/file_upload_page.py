class FileUploadPage:

    def __init__(self, page):
        self.page = page

        self.single_upload = "#singleFileInput"
        self.multiple_upload = "#multipleFilesInput"

    def upload_single_file(self, filepath):

        # scroll to element
        self.page.locator(self.single_upload).scroll_into_view_if_needed()

        # upload file
        self.page.set_input_files(self.single_upload, filepath)
