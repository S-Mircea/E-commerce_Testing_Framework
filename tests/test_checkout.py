import pytest
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.e2e
def test_complete_checkout(logged_in_page: Page, base_url: str):
    """TC-008: Full happy path checkout results in order confirmation."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart(index=0)

    logged_in_page.goto(f"{base_url}/cart.html")
    cart = CartPage(logged_in_page)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_info("John", "Doe", "12345")
    checkout.continue_checkout()
    checkout.finish_order()

    assert "Thank you for your order" in checkout.get_confirmation_text()


def test_checkout_empty_form_validation(logged_in_page: Page, base_url: str):
    """TC-009: Submitting blank checkout form shows First Name required error."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart(index=0)

    logged_in_page.goto(f"{base_url}/cart.html")
    cart = CartPage(logged_in_page)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.continue_checkout()

    assert "First Name is required" in checkout.get_error_message()


def test_logout(logged_in_page: Page, base_url: str):
    """TC-010: Logout via burger menu redirects to login page."""
    inventory = InventoryPage(logged_in_page)
    inventory.logout()

    assert logged_in_page.url == base_url + "/"  or logged_in_page.url == base_url
