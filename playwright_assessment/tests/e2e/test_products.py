
import pytest
from playwright.sync_api import expect


PRODUCTS_URL = "https://ecomcicid.netlify.app/products"


@pytest.mark.e2e
def test_product_listing_visible(shop_page):
    shop_page.goto(PRODUCTS_URL)

    # Product detail links are identified by their URL
    products = shop_page.locator("main a[href*='/products/']")

    expect(products.first).to_be_visible()


@pytest.mark.e2e
def test_product_has_image(shop_page):
    shop_page.goto(PRODUCTS_URL)

    products = shop_page.locator("main a[href*='/products/']")
    first_product = products.first

    expect(first_product).to_be_visible()
    expect(first_product.locator("img").first).to_be_visible()


@pytest.mark.e2e
def test_product_has_name(shop_page):
    shop_page.goto(PRODUCTS_URL)

    products = shop_page.locator("main a[href*='/products/']")
    first_product = products.first

    expect(first_product).to_be_visible()
    expect(first_product).not_to_be_empty()


@pytest.mark.e2e
def test_search_available(shop_page):
    shop_page.goto(PRODUCTS_URL)

    # Find a search input by its accessible role
    search = shop_page.get_by_role("searchbox")

    expect(search).to_be_visible()


@pytest.mark.e2e
def test_search_no_results(shop_page):
    shop_page.goto(PRODUCTS_URL)

    search = shop_page.get_by_role("searchbox")
    expect(search).to_be_visible()

    search.fill("xyzunknownproduct987")
    search.press("Enter")

    expect(
        shop_page.get_by_text("No results", exact=False)
    ).to_be_visible()
