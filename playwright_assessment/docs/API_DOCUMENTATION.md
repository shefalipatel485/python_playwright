# Northline Store – API Documentation

## 1. Project Information

- Application: Northline Store
- URL: https://ecomcicid.netlify.app/
- Automation: Python, Playwright, Pytest
- API testing: Requests / Playwright APIRequestContext

## 2. API Discovery

The application is a JavaScript-rendered website. Actual API endpoints must be identified through Chrome DevTools before API automation is finalized.

Discovery procedure:

1. Open the application.
2. Press F12.
3. Select Network.
4. Select Fetch/XHR.
5. Refresh the application.
6. Perform product search, product selection, cart and checkout actions.
7. Record the requests and responses.

## 3. Endpoint Inventory

| ID | Feature | Method | Endpoint | Status |
|---|---|---|---|---|
| API-01 | Product listing | GET | To be discovered | Pending |
| API-02 | Single product | GET | To be discovered | Pending |
| API-03 | Unknown product | GET | To be discovered | Pending |
| API-04 | Cart operations | To be discovered | To be discovered | Pending |
| API-05 | Checkout | To be discovered | To be discovered | Pending |

## 4. API Test Scenarios

| ID | Test | Expected Result |
|---|---|---|
| API-01 | Get product list | HTTP 200, non-empty JSON array |
| API-02 | Get single product | HTTP 200 and valid product structure |
| API-03 | Unknown product ID | HTTP 404 or documented error |
| API-04 | Response time | Under 2 seconds for key calls |
| API-05 | Response headers | Correct content type and relevant headers |
| API-06 | Cart/checkout calls | Correct status and payload handling, if present |
| API-07 | Invalid payload | Appropriate 4xx response, if supported |
| API-08 | UI/API consistency | Product names and prices match |
| API-09 | Mock server error | UI displays a graceful error state |

## 5. Product Response Schema

The following is an illustrative schema. Confirm actual property names and data types against the discovered response before using it.

```json
{
  "id": 1,
  "name": "Sample Product",
  "price": 49.99,
  "image": "product-image-url"
}
```

## 6. Security and Data Handling

- Do not store passwords or private tokens in source code.
- Do not submit real customer information.
- Do not submit real payments.
- Do not expose sensitive request headers in reports.

## 7. Current Limitations

The actual API endpoint inventory has not yet been verified. This document must be updated after DevTools discovery.

No unverified endpoint should be reported as successfully tested.

## 8. Conclusion

API test completion depends on discovering the actual application data sources and verifying their responses.