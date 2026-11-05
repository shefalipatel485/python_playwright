
import pytest

BASE_URL = "https://ecomcicid.netlify.app"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def shop_page(page, base_url):
    page.goto(base_url)
    return page
