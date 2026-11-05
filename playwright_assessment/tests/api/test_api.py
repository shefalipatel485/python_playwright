
import requests
import pytest

BASE_URL = "https://ecomcicid.netlify.app"


@pytest.mark.api
def test_homepage_status():

    response = requests.get(
        BASE_URL,
        timeout=20
    )

    assert response.status_code == 200


@pytest.mark.api
def test_content_type():

    response = requests.get(
        BASE_URL,
        timeout=20
    )

    assert "text/html" in response.headers[
        "Content-Type"
    ]


@pytest.mark.api
def test_response_time():

    import time

    start = time.time()

    response = requests.get(
        BASE_URL,
        timeout=20
    )

    end = time.time()

    assert response.status_code == 200
    assert end - start < 2


@pytest.mark.api
def test_unknown_route():

    response = requests.get(
        BASE_URL + "/unknown-test-route",
        timeout=20
    )

    assert response.status_code < 500


@pytest.mark.api
def test_html_response():

    response = requests.get(
        BASE_URL,
        timeout=20
    )

    assert "<html" in response.text.lower()


@pytest.mark.api
def test_robots_txt():

    response = requests.get(
        BASE_URL + "/robots.txt",
        timeout=20
    )

    assert response.status_code in [200, 301, 302, 404]


@pytest.mark.api
def test_sitemap():

    response = requests.get(
        BASE_URL + "/sitemap.xml",
        timeout=20
    )

    assert response.status_code in [200, 301, 302, 404]


@pytest.mark.api
def test_invalid_product_endpoint_not_assumed():

    # Product API endpoint must first be discovered
    # using browser DevTools Network tab.

    assert BASE_URL.startswith("https://")
