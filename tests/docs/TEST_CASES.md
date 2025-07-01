# Test Case Specification - Personal Budget Tracker

## TDD/Documentation Workflow (reminder)

1. Add a new row in TEST_CASES.md (define test case)
2. Write the test (in tests/)
3. Run the test (expect failure)
4. Write implementation code (just enough to pass)
5. Run the test again (expect success)
6. Update the test case status to PASS or FAIL
7. Document result in TEST_REPORT.md
8. Refactor implementation -> Re-run all tests

## Module: Transaction Model

| Test ID  | Description                      | Input                                                                                 | Expected Output                  | Status |
|----------|----------------------------------|---------------------------------------------------------------------------------------|----------------------------------|--------|
| TC-TM-01 | Create valid expense transaction | amount=25.50, type="expense", category="Food", description="Lunch", date="2025-06-30" | Transaction created successfully | PASS   |
| TC-TM-02 | Reject negative amount           | amount=-10.0                                                                          | ValueError raised                | PASS   |
| TC-TM-03 | Reject invalid type              | type="spending"                                                                       | ValueError raised                | PASS   |
| TC-TM-04 | Allow optional description       | description not provided                                                              | Transaction created successfully | PASS   |
| TC-TM-05 | Reject empty category variable   | category = ""                                                                         | ValueError raised                | PASS   |


---

## Module: BudgetManager

| Test ID  | Description                        | Input                                               | Expected Output                 | Status |
|----------|------------------------------------|-----------------------------------------------------|----------------------------------|--------|
| TC-BM-01 | Add valid transaction              | Transaction instance                                | Added and stored successfully   |        |
| TC-BM-02 | Get all transactions               | (no input)                                          | List of all transactions        |        |
| TC-BM-03 | Calculate correct balance          | 2 incomes + 3 expenses                              | Correct net total               |        |
| TC-BM-04 | Filter transactions by category    | category="Food"                                     | Only Food transactions returned |        |

---

## Module: DatabaseManager

| Test ID  | Description                        | Input                                               | Expected Output                 | Status |
|----------|------------------------------------|-----------------------------------------------------|----------------------------------|--------|
| TC-DB-01 | Save transaction to database       | Valid Transaction                                   | Record inserted successfully    |        |
| TC-DB-02 | Retrieve transactions from DB      | Query all                                           | Correct data returned           |        |
| TC-DB-03 | Reject duplicate primary key       | Duplicate ID                                        | IntegrityError raised           |        |
| TC-DB-04 | Handle empty DB case               | Empty transaction table                             | Empty list returned             |        |

---

## Module: Transaction Repository

| Test ID    | Description                   | Input                    | Expected Output               | Status |
|------------|-------------------------------|--------------------------|-------------------------------|--------|
| TC-REPO-01 | Add transaction to database   | Valid Transaction object | Transaction saved in database | PASS   |
| TC-REPO-02 | Retrieve transactions from DB | Query all                | Correct data returned         | PASS   |
| TC-REPO-03 | Reject duplicate primary key  | Duplicate ID             | IntegrityError raised         |        |
| TC-REPO-04 | Handle empty DB case          | Empty transaction table  | Empty list returned           |        |

---

## Module: Main App UI

| Test ID  | Description                   | Input                    | Expected Output               | Status |
|----------|-------------------------------|--------------------------|-------------------------------|--------|
| TC-UI-01 | Add transaction to database   | Valid Transaction object | Transaction saved in database | PASS   |
| TC-UI-02 | Retrieve transactions from DB | Query all                | Correct data returned         | PASS   |
| TC-UI-03 | Reject duplicate primary key  | Duplicate ID             | IntegrityError raised         |        |
| TC-UI-04 | Handle empty DB case          | Empty transaction table  | Empty list returned           |        |