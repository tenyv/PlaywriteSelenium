import pytest
from pages.demo_test_record import DemoTestRecord
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture
def demo(page):
    obj = DemoTestRecord(page)
    obj.navigate("https://practicetestautomation.com/practice-test-login/")
    return obj

def test_demo_test_login(demo,page):
    demo.login("student","Password123")
    demo.submit()
    expect(page.get_by_role("heading")).to_contain_text("Logged In Successfully")

def test_click_link(demo,page):
    demo.clickOnLink("Courses")
    expect(page.locator("h1")).to_contain_text("Courses")

