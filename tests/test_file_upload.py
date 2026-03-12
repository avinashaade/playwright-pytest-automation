from pages.file_upload_page import FileUploadPage


def test_file_upload(page):

    page.goto("https://testautomationpractice.blogspot.com/")

    upload = FileUploadPage(page)

    file_path = r"C:\Users\Avinash Aade\Downloads\Avinash_Aade_Harvard_Resume.pdf"

    upload.upload_single_file(file_path)

    assert page.locator("#singleFileInput").is_visible()