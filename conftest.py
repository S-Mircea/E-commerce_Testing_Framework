import pytest
from pathlib import Path
from playwright.sync_api import Page

PROJECT_ROOT = Path(__file__).parent
TEST_RESULTS = PROJECT_ROOT / "test-results"
SCREENSHOTS_DIR = TEST_RESULTS / "screenshots"


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: Quick sanity check tests")
    config.addinivalue_line("markers", "regression: Full regression suite")
    config.addinivalue_line("markers", "e2e: End-to-end critical path")
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def logged_in_page(page: Page, base_url: str) -> Page:
    """Navigate to the site and log in as standard_user, yielding an authenticated page."""
    page.goto(base_url)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    yield page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page: Page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")
        if page:
            SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
            safe_name = item.nodeid.replace("/", "_").replace("::", "_")
            page.screenshot(path=str(SCREENSHOTS_DIR / f"{safe_name}.png"))
