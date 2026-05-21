import pytest
import os
from playwright.sync_api import sync_playwright


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        item.failed = True


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser


@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()
    yield page

    # Take screenshot only if test failed
    if hasattr(request.node, "failed") and request.node.failed:

        test_name = request.node.name
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
        print("→ Screenshot WILL BE TAKEN:", screenshot_path)
        page.screenshot(path=screenshot_path)

    context.close()