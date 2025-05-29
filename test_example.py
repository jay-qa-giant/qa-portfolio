# from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from login_page import LoginPage
import pytest

@pytest.mark.regression
def test_valid_login(page):
        login_page = LoginPage(page)
        login_page.login(page, "student", "Password123")
        login_page.verify_valid_login(page)
       
        
@pytest.mark.regression
@pytest.mark.smoke        
def test_negative_username(page):
        login_page = LoginPage(page)
        login_page.login(page, "incorrectUser", "Password123")
        expect(page.locator("#error")).to_be_visible()
        