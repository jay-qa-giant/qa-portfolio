import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from login_page import LoginPage
from playwright.sync_api import expect

scenarios('../../login.feature')

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@given("I am on the login page")
def go_to_login_page(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login(login_page, username, password):
    login_page.login(login_page.page, username, password)

@then("I should see the successful login page")
def verify_success(login_page):
    login_page.verify_valid_login(login_page.page)

@then("I should see an error message")
def verify_error(page):
    expect(page.locator("#error")).to_be_visible()