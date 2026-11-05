
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.e2e
def test_home_page_loads(shop_page):
    expect(shop_page).to_have_title("Northline Store")


@pytest.mark.e2e
def test_home_page_body_visible(shop_page):
    expect(shop_page.locator("body")).to_be_visible()


@pytest.mark.e2e
def test_navigation_visible(shop_page):
    navigation = shop_page.get_by_role("navigation")
    expect(navigation).to_be_visible()


@pytest.mark.e2e
def test_footer_visible(shop_page):
    # Select the main website footer, not testimonial footers
    footer = shop_page.get_by_role("contentinfo")
    expect(footer).to_be_visible()


@pytest.mark.e2e
def test_page_has_heading(shop_page):
    heading = shop_page.get_by_role("heading").first
    expect(heading).to_be_visible()
