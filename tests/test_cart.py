import pytest
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_to_cart(logged_in_page: Page):
    """TC-006: Adding a product shows badge count of 1."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart(index=0)
    assert inventory.get_cart_badge_count() == "1"


def test_remove_from_cart(logged_in_page: Page, base_url: str):
    """TC-007: Removing the only cart item empties the cart."""
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart(index=0)

    logged_in_page.goto(f"{base_url}/cart.html")
    cart = CartPage(logged_in_page)
    cart.remove_first_item()

    assert cart.get_item_count() == 0
    assert logged_in_page.locator('.shopping_cart_badge').count() == 0
