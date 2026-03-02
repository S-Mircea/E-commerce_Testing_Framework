import pytest
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage


def test_products_displayed(logged_in_page: Page):
    """TC-004: Exactly 6 products are displayed on the inventory page."""
    inventory = InventoryPage(logged_in_page)
    assert inventory.get_item_count() == 6


def test_sort_by_price_low_to_high(logged_in_page: Page):
    """TC-005: Sorting by price low-to-high re-orders products correctly."""
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("lohi")

    prices = logged_in_page.locator('.inventory_item_price').all_inner_texts()
    price_values = [float(p.replace('$', '')) for p in prices]
    assert price_values == sorted(price_values), (
        f"Prices are not sorted ascending: {price_values}"
    )
