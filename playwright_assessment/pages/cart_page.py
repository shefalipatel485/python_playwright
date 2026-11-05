
from pages.base_page import BasePage


class CartPage(BasePage):

    def open_cart(self):
        self.page.get_by_role(
            "link",
            name="Cart"
        ).click()

    def get_cart_items(self):
        return self.page.locator(
            '[data-testid="cart-item"]'
        )

    def remove_item(self):
        self.page.get_by_role(
            "button",
            name="Remove"
        ).click()
