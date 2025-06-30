# Test Plan - Personal Budget Tracker

## Project Overview
This project is a personal budgeting application built with Python, using `tkinter` for the GUI, `sqlite3` for data storage, and a modular backend with test-driven development.

---

## Objective
Ensure correctness, reliability, and maintainability of the budget tracking features through automated and manual testing.

---

## Test Scope

### In-Scope
- Unit tests for:
  - `Transaction` data model validation
  - `BudgetManager` business logic
  - Database interactions (CRUD)
- Integration tests:
  - BudgetManager + Database interaction
- Smoke tests on GUI (manual)

### Out of Scope
- Full GUI automation testing
- Performance and load testing

---

## Tools and Frameworks

| Tool       | Purpose                    |
|------------|----------------------------|
| `pytest`   | Test execution framework   |
| `sqlite3`  | Lightweight DB for storage |
| `pytest-cov` | (Optional) Coverage reports |
| `black` / `flake8` | Code formatting/linting |

---

## Test Types

| Type              | Description                                |
|-------------------|--------------------------------------------|
| Unit Testing      | Isolated testing of model and logic layers |
| Integration Testing | DB operations with real data              |
| Manual GUI Testing| Ensure forms/buttons work as expected      |

---

## Test Environment

- Python 3.10
- Virtual environment (`venv`)
- OS: Windows 10 / macOS / Linux
- PyCharm IDE with pytest integration

---

## Roles and Responsibilities
As the sole developer, I am responsible for test design, implementation, execution, and documentation.

---

## Risks and Assumptions
- GUI may have limited test automation coverage due to tkinter limitations.
- SQLite is assumed to behave consistently between environments.
