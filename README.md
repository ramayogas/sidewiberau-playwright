# SIDEWIBERAU Playwright

Web UI automation testing project for [SIDEWIBERAU](https://sidewiberau.com/) using **Python** and **Playwright**.

This project is built as a QA automation portfolio to practice and demonstrate:

* Test scenario and test case design
* Web UI automation
* Functional testing
* Positive and negative testing
* Assertions and validation
* Test execution and reporting

## Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming language |
| Playwright   | Web automation       |
| Git & GitHub | Version control      |

## Project Structure

```text
sidewiberau-playwright/
│
├── README.md
├── requirements.txt
│
├── test-cases/
│   └── login.md
│
├── tests/
│   └── login.py
│
└── screenshots/
```

## Testing Scope

The project currently focuses on the publicly accessible SIDEWIBERAU web application.

Initial testing scope:

* Login page
* Guest login
* Website navigation
* Functional UI behavior

The testing scope will be expanded as the project develops.

## Test Cases

Test cases are documented separately from the automation scripts.

Example:

```text
test-cases/
└── login.md
```

Each test case contains:

* Test Case ID
* Test Scenario
* Description
* Preconditions
* Test Data
* Test Steps
* Expected Result
* Test Type
* Priority
* Constraints / Limitations

## Automation

The test cases are automated using Playwright.

Example:

```text
test-cases/login.md
        ↓
   Test Design
        ↓
tests/login.py
        ↓
 Playwright
        ↓
 Test Execution
```

## Current Test Coverage

| Feature | Test Case           | Automation |
| ------- | ------------------- | ---------- |
| Login   | Open Login Page     | ✅          |
| Login   | Login as Guest      | ✅          |
| Login   | Invalid credentials | ⬜          |
| Login   | Empty credentials   | ⬜          |

> Test coverage will be updated as additional scenarios are automated.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ramayogas/sidewiberau-playwright.git
cd sidewiberau-playwright
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```bash
playwright install
```

### 4. Run the test

```bash
python tests/login.py
```

## Test Results

Test execution results and reporting will be added as the automation framework develops.

## Notes

This project is created for learning and portfolio purposes.

Testing is performed against the publicly accessible version of the application. The application, its data, and its behavior may change over time.

## Author

**Rama Yogaswara**

