from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
    
    def login(self, page, username, password):
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill(username)
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill(password)
        page.get_by_role("button", name="Submit").click()
        
    def verify_valid_login(self, page):
        url = "https://practicetestautomation.com/logged-in-successfully/"
        expect(page).to_have_url(url)
        expect(page.get_by_text("Congratulations student. You")).to_be_visible()
        expect(page.get_by_role("link", name="Log out")).to_be_visible()