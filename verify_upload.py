
from playwright.sync_api import Page, expect, sync_playwright
import time
import os

def verify_file_upload(page: Page):
    # 1. Load the page
    page.goto("http://localhost:8080/template.html")
    time.sleep(2)

    # Create a dummy file to upload
    with open("test_upload.txt", "w") as f:
        f.write("Hello from Playwright file upload test!")

    # 2. Find the file input and upload
    # Use set_input_files on the input element directly
    try:
        page.set_input_files("#file-input", "test_upload.txt")
        time.sleep(1)

        # 3. Verify content in textarea
        textarea = page.locator("#user-input")
        expect(textarea).to_contain_text("Hello from Playwright file upload test!")
        expect(textarea).to_contain_text("[Arquivo: test_upload.txt]")

        # Screenshot
        page.screenshot(path="verification_upload_fixed.png")

        print("Verification complete.")

    except Exception as e:
        print(f"Error: {e}")
        page.screenshot(path="debug_error_fixed.png")

    # Cleanup
    if os.path.exists("test_upload.txt"):
        os.remove("test_upload.txt")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_file_upload(page)
        finally:
            browser.close()
