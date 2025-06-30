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

| Test ID     | Description                        | Input                                               | Expected Output                 | Status |
|-------------|------------------------------------|-----------------------------------------------------|----------------------------------|--------|
| TC-BM-001   | Add valid transaction              | Transaction instance                                | Added and stored successfully   |        |
| TC-BM-002   | Get all transactions               | (no input)                                          | List of all transactions        |        |
| TC-BM-003   | Calculate correct balance          | 2 incomes + 3 expenses                              | Correct net total               |        |
| TC-BM-004   | Filter transactions by category    | category="Food"                                     | Only Food transactions returned |        |

---

## Module: DatabaseManager / Repository

| Test ID     | Description                        | Input                                               | Expected Output                 | Status |
|-------------|------------------------------------|-----------------------------------------------------|----------------------------------|--------|
| TC-DB-001   | Save transaction to database       | Valid Transaction                                   | Record inserted successfully    |        |
| TC-DB-002   | Retrieve transactions from DB      | Query all                                           | Correct data returned           |        |
| TC-DB-003   | Reject duplicate primary key       | Duplicate ID                                        | IntegrityError raised           |        |
| TC-DB-004   | Handle empty DB case               | Empty transaction table                             | Empty list returned             |        |
