import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_valid_login(page: Page, base_url: str):
    """TC-001: Valid login redirects to inventory page."""
    login = LoginPage(page)
    login.navigate(base_url)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url


def test_invalid_password(page: Page, base_url: str):
    """TC-002: Wrong password shows error message."""
    login = LoginPage(page)
    login.navigate(base_url)
    login.login("standard_user", "wrong_pass")
    assert "Username and password do not match" in login.get_error_message()


def test_locked_out_user(page: Page, base_url: str):
    """TC-003: Locked out user sees locked-out error."""
    login = LoginPage(page)
    login.navigate(base_url)
    login.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out" in login.get_error_message()
