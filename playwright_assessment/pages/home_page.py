
from pages.base_page import BasePage


class HomePage(BasePage):

    def get_navigation(self):
        return self.page.get_by_role("navigation")

    def get_products(self):
        return self.page.locator(
            '[data-testid="product-card"]'
        )

    def get_search(self):
        return self.page.get_by_role(
            "searchbox"
        )
