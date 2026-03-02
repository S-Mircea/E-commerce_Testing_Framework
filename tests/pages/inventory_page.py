from playwright.sync_api import Page
from .base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_title = page.locator('.title')
        self.inventory_items = page.locator('.inventory_item')
        self.sort_dropdown = page.locator('select.product_sort_container')
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.burger_menu = page.locator('#react-burger-menu-btn')
        self.logout_link = page.locator('#logout_sidebar_link')

    def get_item_count(self) -> int:
        return self.inventory_items.count()

    def add_item_to_cart(self, index: int = 0):
        add_buttons = self.page.locator('[data-test^="add-to-cart"]')
        add_buttons.nth(index).click()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    def get_cart_badge_count(self) -> str:
        return self.cart_badge.inner_text()

    def logout(self):
        self.burger_menu.click()
        self.logout_link.click()
