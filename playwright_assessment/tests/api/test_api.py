
import pytest
import requests
import time

BASE_URL = (
    "https://681444af225ff1af16285b31.mockapi.io/electronicapi"
)


# 1. Get all products
@pytest.mark.api
def test_get_all_products():

    response = requests.get(BASE_URL, timeout=10)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# 2. Verify product response structure
@pytest.mark.api
def test_product_response_structure():

    response = requests.get(BASE_URL, timeout=10)

    assert response.status_code == 200

    products = response.json()

    assert len(products) > 0

    product = products[0]

    required_fields = [
        "id",
        "name",
        "price",
        "brand",
        "category",
        "rating",
        "stock"
    ]

    for field in required_fields:
        assert field in product


# 3. Get a single product
@pytest.mark.api
def test_get_single_product():

    response = requests.get(
        f"{BASE_URL}/1",
        timeout=10
    )

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == "1"
    assert product["name"] == "Skullcandy Crusher Evo"


# 4. Get invalid product ID
@pytest.mark.api
def test_get_invalid_product():

    response = requests.get(
        f"{BASE_URL}/999999",
        timeout=10
    )

    assert response.status_code == 404


# 5. Verify response headers
@pytest.mark.api
def test_response_headers():

    response = requests.get(BASE_URL, timeout=10)

    assert response.status_code == 200

    content_type = response.headers.get(
        "Content-Type", ""
    )

    assert "application/json" in content_type


# 6. Verify API response time
@pytest.mark.api
def test_api_response_time():

    start_time = time.perf_counter()

    response = requests.get(BASE_URL, timeout=10)

    end_time = time.perf_counter()

    response_time = end_time - start_time

    assert response.status_code == 200
    assert response_time < 2.0

    print(f"API Response Time: {response_time:.3f} seconds")


# 7. Create a new product
@pytest.mark.api
def test_create_product():

    new_product = {
        "name": "Test Automation Headphones",
        "price": "15000",
        "brand": "TestBrand",
        "category": "Headphones",
        "rating": "4.5",
        "stock": "20",
        "description": "Created using Pytest API automation",
        "image": "https://picsum.photos/400/400"
    }

    response = requests.post(
        BASE_URL,
        json=new_product,
        timeout=10
    )

    assert response.status_code == 201

    created_product = response.json()

    assert "id" in created_product
    assert created_product["name"] == new_product["name"]

    # Clean up the created test record
    product_id = created_product["id"]

    delete_response = requests.delete(
        f"{BASE_URL}/{product_id}",
        timeout=10
    )

    assert delete_response.status_code == 200


# 8. Update and delete a product
@pytest.mark.api
def test_update_and_delete_product():

    new_product = {
        "name": "Temporary Test Product",
        "price": "10000",
        "brand": "TestBrand",
        "category": "Electronics",
        "rating": "4.0",
        "stock": "10"
    }

    # Create product
    create_response = requests.post(
        BASE_URL,
        json=new_product,
        timeout=10
    )

    assert create_response.status_code == 201

    product_id = create_response.json()["id"]

    try:
        # Update product
        update_response = requests.patch(
            f"{BASE_URL}/{product_id}",
            json={"price": "12000"},
            timeout=10
        )

        assert update_response.status_code == 200
        assert update_response.json()["price"] == "12000"

        # Verify updated product
        get_response = requests.get(
            f"{BASE_URL}/{product_id}",
            timeout=10
        )

        assert get_response.status_code == 200
        assert get_response.json()["price"] == "12000"

        # Delete product
        delete_response = requests.delete(
            f"{BASE_URL}/{product_id}",
            timeout=10
        )

        assert delete_response.status_code == 200

        # Verify deletion
        verify_response = requests.get(
            f"{BASE_URL}/{product_id}",
            timeout=10
        )

        assert verify_response.status_code == 404

    finally:
        # Try cleanup if the test fails before deletion
        requests.delete(
            f"{BASE_URL}/{product_id}",
            timeout=10
        )
