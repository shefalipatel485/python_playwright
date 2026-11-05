
from pages.base_page import BasePage


class ProductPage(BasePage):

    def add_to_cart(self):
        self.page.get_by_role(
            "button",
            name="Add to Cart"
        ).click()

    def get_product_name(self):
        return self.page.get_by_role(
            "heading",
            level=1
        )
