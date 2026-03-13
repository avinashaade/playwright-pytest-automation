from pages.file_upload_page import FileUploadPage


def test_file_upload(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    upload = FileUploadPage(page)

    file_path = "tests/test_data/upload_file.png"

    upload.upload_single_file(file_path)

    assert page.locator("#singleFileInput").is_visible()