
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def enter_email(self, email):
        self.page.get_by_label(
            "Email"
        ).fill(email)

    def enter_name(self, name):
        self.page.get_by_label(
            "Full Name"
        ).fill(name)

    def submit_order(self):
        self.page.get_by_role(
            "button",
            name="Place Order"
        ).click()
