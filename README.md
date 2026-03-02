# E-Commerce Testing Framework

![Tests](https://github.com/S-Mircea/E-commerce_Testing_Framework/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Playwright](https://img.shields.io/badge/playwright-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

A professional automated end-to-end testing suite for [SauceDemo](https://www.saucedemo.com), a purpose-built QA practice application. This project demonstrates real-world QA engineering skills: manual test planning, UI automation with Playwright + Pytest, Page Object Model (POM) design pattern, GitHub Actions CI/CD, and structured bug reporting.

---

## Features

- **10 automated test cases** covering login, inventory, cart, checkout, and session management
- **Page Object Model** for clean separation of locators and test logic
- **HTML test reports** with automatic screenshot capture on failure
- **GitHub Actions CI/CD** — tests run automatically on every push and pull request
- **Professional bug report** documenting a real observable defect

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Test language |
| Playwright | Browser automation |
| pytest | Test runner |
| pytest-playwright | Playwright integration for pytest |
| pytest-html | HTML test report generation |
| GitHub Actions | CI/CD pipeline |

---

## Project Structure

```
E-commerce_Testing_Framework/
├── .github/
│   └── workflows/
│       └── tests.yml              # GitHub Actions CI/CD
├── docs/
│   └── test_cases.md              # Manual test plan (10 test cases)
├── tests/
│   ├── conftest.py                # Fixtures, hooks, screenshot-on-failure
│   ├── pages/                     # Page Object Model classes
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── test_login.py              # TC-001 to TC-003
│   ├── test_inventory.py          # TC-004 to TC-005
│   ├── test_cart.py               # TC-006 to TC-007
│   └── test_checkout.py           # TC-008 to TC-010
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/S-Mircea/E-commerce_Testing_Framework.git
cd E-commerce_Testing_Framework

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browser
playwright install chromium
```

### Running Tests

```bash
# Run all tests (generates HTML report at test-results/report.html)
pytest

# Run only smoke tests
pytest -m smoke

# Run only end-to-end critical path tests
pytest -m e2e

# Run a specific test file
pytest tests/test_login.py

# Run with Playwright traces retained on failure
pytest --tracing=retain-on-failure
```

### Viewing the Report

After running tests, open the HTML report:

```bash
open test-results/report.html
```

---

## Test Cases

| TC ID | Title | Priority |
|-------|-------|----------|
| TC-001 | Valid login — standard user | High |
| TC-002 | Invalid login — wrong password | High |
| TC-003 | Locked out user cannot log in | High |
| TC-004 | Products listed on inventory page | Medium |
| TC-005 | Sort products by price (low to high) | Medium |
| TC-006 | Add product to cart | High |
| TC-007 | Remove product from cart | Medium |
| TC-008 | Complete checkout — happy path | Critical |
| TC-009 | Checkout blocked with empty form | High |
| TC-010 | Logout via burger menu | Medium |

See [docs/test_cases.md](docs/test_cases.md) for full test case details including steps and expected results.

---

## CI/CD

Tests run automatically on every push and pull request to `main` via GitHub Actions. The workflow:

1. Sets up Python 3.12
2. Installs dependencies from `requirements.txt`
3. Installs Chromium via Playwright
4. Runs the full test suite
5. Uploads the HTML test report as a build artifact (retained 30 days)

Download the `test-report` artifact from the Actions tab to view results for any CI run.

---

## Bug Report

### BUG-001: Locked Out User Receives No Actionable Error Guidance

**Severity:** High
**Environment:** SauceDemo — https://www.saucedemo.com
**Browser:** Chromium (latest)
**Discovered by:** Automated test TC-003

**Steps to Reproduce:**
1. Navigate to https://www.saucedemo.com
2. Enter username: `locked_out_user`
3. Enter password: `secret_sauce`
4. Click the "Login" button

**Expected Result:**
User should receive a clear message explaining their account status
and instructions on how to contact support or unlock their account.

**Actual Result:**
User sees a generic error: *"Epic sadface: Sorry, this user has been locked out."*
No guidance, no support link, and no account recovery option is provided.

**Impact:**
A real user would have no path forward. This poor UX could result in
customer churn or unnecessary support tickets — a measurable business cost.

**Evidence:** Screenshot captured automatically by the test suite on failure.

---

## License

MIT
