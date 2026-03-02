from playwright.sync_api import Page
from .base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.error_message = page.locator('[data-test="error"]')
        self.confirmation_header = page.locator('.complete-header')

    def fill_info(self, first: str, last: str, zip_code: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def get_confirmation_text(self) -> str:
        return self.confirmation_header.inner_text()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()
