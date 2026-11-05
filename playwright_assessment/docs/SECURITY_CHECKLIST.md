# Northline Store – Security Checklist

## 1. Objective

This checklist records basic security-related checks and safe testing practices during automation.

This is not a penetration-testing report.

## 2. HTTPS Checks

- [ ] Website is accessed using HTTPS.
- [ ] HTTP redirects to HTTPS, if configured.
- [ ] No mixed-content warnings are observed.

## 3. Data Protection

- [ ] No real customer data is used.
- [ ] No real payment information is submitted.
- [ ] No passwords are stored in source code.
- [ ] Sensitive information is excluded from screenshots and logs.

## 4. Repository Security

- [ ] No API keys are committed.
- [ ] No authentication tokens are committed.
- [ ] `.env` files are excluded from Git.
- [ ] GitHub Secrets are used for required credentials.
- [ ] Dependencies are reviewed.

## 5. API Response Review

- [ ] Actual response content types are checked.
- [ ] Sensitive information is not unnecessarily exposed.
- [ ] Error responses do not expose unnecessary internal details.
- [ ] Request and response logs are reviewed for sensitive data.

## 6. Checkout Safety

- [ ] Checkout validation is tested with synthetic data.
- [ ] Real payment processing is not performed.
- [ ] No actual customer order is submitted.

## 7. Reporting

| Check | Status | Remarks |
|---|---|---|
| HTTPS | Pending | Verify during execution |
| Secrets in repository | Pending | Review Git repository |
| Sensitive data in logs | Pending | Review test reports |
| Checkout safety | Pending | Use test data only |
| Dependency review | Pending | Review requirements |

## 8. Final Assessment

Complete this checklist after inspecting the application, repository and test execution evidence.

No penetration testing or security certification is claimed by this checklist.