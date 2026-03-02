# Manual Test Cases — SauceDemo E-Commerce Testing Framework

**Target Site:** https://www.saucedemo.com
**Test Environment:** Chromium (latest)
**Credentials used:**
- `standard_user / secret_sauce` — Happy path user
- `locked_out_user / secret_sauce` — Account locked
- `standard_user / wrong_pass` — Invalid credentials

---

## Test Cases

| TC ID | Title | Preconditions | Steps | Expected Result | Priority | Status |
|-------|-------|---------------|-------|-----------------|----------|--------|
| TC-001 | Valid login — standard user | User is on login page | 1. Enter username: `standard_user` <br> 2. Enter password: `secret_sauce` <br> 3. Click "Login" | User is redirected to `/inventory.html`. Products page is displayed. | High | Automated |
| TC-002 | Invalid login — wrong password | User is on login page | 1. Enter username: `standard_user` <br> 2. Enter password: `wrong_pass` <br> 3. Click "Login" | Error message displayed: "Epic sadface: Username and password do not match any user in this service" | High | Automated |
| TC-003 | Locked out user cannot log in | User is on login page | 1. Enter username: `locked_out_user` <br> 2. Enter password: `secret_sauce` <br> 3. Click "Login" | Error message displayed: "Epic sadface: Sorry, this user has been locked out." | High | Automated |
| TC-004 | Products listed on inventory page | User is logged in as `standard_user` | 1. Navigate to `/inventory.html` | Exactly 6 product items are displayed on the inventory page. | Medium | Automated |
| TC-005 | Sort products by price (low to high) | User is logged in and on inventory page | 1. Open the sort dropdown <br> 2. Select "Price (low to high)" | Products are re-ordered: cheapest item first, most expensive last. First item price ≤ last item price. | Medium | Automated |
| TC-006 | Add product to cart | User is logged in and on inventory page | 1. Click "Add to cart" on any product | Shopping cart badge appears showing count "1". | High | Automated |
| TC-007 | Remove product from cart | User has 1 item in cart | 1. Navigate to `/cart.html` <br> 2. Click "Remove" on the first cart item | Cart item list is empty. Cart badge disappears from the header. | Medium | Automated |
| TC-008 | Complete checkout — happy path | User is logged in and has 1 item in cart | 1. Navigate to cart <br> 2. Click "Checkout" <br> 3. Fill in First Name, Last Name, Zip Code <br> 4. Click "Continue" <br> 5. Click "Finish" | Confirmation page displays "Thank you for your order!" | Critical | Automated |
| TC-009 | Checkout blocked with empty form | User is logged in, has item in cart, is on checkout step one | 1. Leave all fields blank <br> 2. Click "Continue" | Error message displayed: "Error: First Name is required" | High | Automated |
| TC-010 | Logout via burger menu | User is logged in on any page | 1. Click the burger menu icon (top-left) <br> 2. Click "Logout" | User is redirected to the login page (`/`). Session is terminated. | Medium | Automated |

---

## Test Coverage Summary

| Feature Area | Test Cases | Coverage |
|---|---|---|
| Authentication | TC-001, TC-002, TC-003 | Login (valid, invalid password, locked account) |
| Product Catalogue | TC-004, TC-005 | Display count, sorting |
| Shopping Cart | TC-006, TC-007 | Add to cart, remove from cart |
| Checkout Flow | TC-008, TC-009 | Full happy path, form validation |
| Navigation / Session | TC-010 | Logout |

---

## Known Issues / Bug Reports

See [README.md](../README.md#bug-report) for documented bugs found during testing.
