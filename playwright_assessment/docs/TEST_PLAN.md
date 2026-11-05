# Northline Store – Test Plan

## 1. Objective

The objective is to validate the Northline Store e-commerce website through automated browser and HTTP testing using Python Playwright and Pytest.

## 2. Application Under Test

URL: https://ecomcicid.netlify.app/

## 3. Scope of Testing

### In Scope

- Homepage
- Navigation
- Product listing
- Product details
- Search
- Filtering and sorting
- Shopping cart
- Quantity update
- Cart removal
- Shipping threshold
- Checkout validation
- Order confirmation
- Cart persistence, if supported
- Responsive layout
- API/data-source checks
- Cross-browser testing

### Out of Scope

- Load and performance testing
- Penetration testing
- Real payment processing

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11+ | Programming language |
| Playwright | Browser automation |
| Pytest | Test execution |
| pytest-playwright | Pytest browser integration |
| pytest-html | HTML reporting |
| pytest-xdist | Parallel execution |
| Requests | HTTP testing |
| Faker | Test data generation |
| jsonschema | JSON response validation |
| GitHub Actions | CI/CD |

## 5. Browser Coverage

- Chromium
- Firefox
- WebKit

## 6. Test Viewports

| Device | Viewport |
|---|---|
| Desktop | 1366 × 768 |
| Mobile | 390 × 844 |

## 7. Test Execution Strategy

### Smoke Testing

Execute critical tests first:

- Homepage loads.
- Navigation is available.
- Product listing is visible.
- Product can be opened.
- Critical cart functionality works.

### Regression Testing

Execute all confirmed functional test cases.

### API Testing

Execute tests against the actual discovered endpoints or data sources.

### Responsive Testing

Verify usability at desktop and mobile viewport sizes.

## 8. Test Execution Commands

```bash
pytest -m smoke
pytest -m "e2e and not smoke"
pytest tests/api
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
pytest -n 4
```

## 9. Acceptance Criteria

- At least 20 E2E tests.
- At least 8 API tests.
- Smoke tests pass on Chromium, Firefox and WebKit.
- Full suite is stable across three consecutive CI runs.
- Pull requests automatically execute the tests.
- Failed tests include screenshots and Playwright traces.
- No hard-coded sleeps.
- Locators use accessible roles or stable test IDs wherever possible.

## 10. Test Data and Safety

- Use synthetic test data.
- Do not enter real customer details.
- Do not process real payments.
- Keep each test independent.
- Avoid creating real orders.

## 11. Final Result

The final test result will be recorded after execution and defect verification.