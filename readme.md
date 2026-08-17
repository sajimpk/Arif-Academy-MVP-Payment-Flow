# Arif Academy Automation MVP

This repository contains the BDD (Behavior-Driven Development) test automation suite for the [Arif Academy](https://arifacademy.com/) platform. Built with Python, Behave (Cucumber implementation), and Selenium Webdriver, it automates testing for core workflows including user authentication and purchase flows up to the SSLCommerz payment gateway.

---

## Project Structure

```text
├── features/
│   ├── locators/
│   │   └── locators.py         # Separated UI page locators (POM style)
│   ├── steps/
│   │   ├── login_steps.py      # Steps mapping to login.feature
│   │   └── purchase_steps.py   # Steps mapping to purchase.feature
│   ├── environment.py          # Browser lifecycle setup and hooks
│   ├── login.feature           # Authentication BDD test scenarios
│   └── purchase.feature        # Purchase/Checkout BDD test scenarios
├── .gitignore
├── requirements.txt
└── readme.md
```

---

## Setup & Installation

### 1. Prerequisites
- Python 3.10+ installed on your system.
- Google Chrome browser installed (the framework manages the ChromeDriver version automatically).

### 2. Configure Virtual Environment
Initialize and activate your virtual environment:
```powershell
# Create venv
python -m venv .venv

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Dependencies include: `selenium`, `behave`, `webdriver-manager`)*

---

## Running the Tests

To run all scenarios across all feature files:
```bash
behave
```

To run a specific feature file:
```bash
behave features/purchase.feature
```

---

## Key Scenarios Covered

1. **Verify Home Page Accessibility**: Checks that the primary landing page loads properly and page titles match brand parameters.
2. **Login Redirects**: Enters user credentials and ensures proper dashboard landing.
3. **Purchase Flow (With Login)**: Simulates a logged-in user purchasing the IELTS CBT Mock Mastery (1-Month) package, completing the billing checkout, and verifying the redirect to SSLCommerz.
4. **Purchase Flow (Without Login)**: Simulates a guest user trying to checkout, redirects them to the login flow first, and successfully returns them back to checkout to complete the payment gateway routing.
