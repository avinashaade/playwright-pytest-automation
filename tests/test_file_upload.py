from pages.file_upload_page import FileUploadPage


def test_file_upload(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    upload = FileUploadPage(page)

    file_path = r"C:\Users\Avinash Aade\Desktop\Screenshot 2026-03-13 134228.png"

    upload.upload_single_file(file_path)

    assert page.locator("#singleFileInput").is_visible()