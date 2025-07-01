import sqlite3
import copy
import pytest

from budget_tracker.models.transaction import Transaction
from budget_tracker.persistence.transaction_repo import TransactionRepository
from budget_tracker.persistence.database_manager import create_connection, initialize_database

# Sample transaction data
base_data = {
    "amount": 25.50,
    "type": "expense",
    "category": "Food",
    "description": "Lunch",
    "date": "2025-06-30"
}

@pytest.fixture
def db_connection():
    # Set up a fresh in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    initialize_database(conn) # creates the transactions table
    yield conn
    conn.close()

def test_add_transaction_saves_to_db(db_connection):
    repo = TransactionRepository(db_connection)
    data = copy.deepcopy(base_data)
    tx = Transaction(**data)

    repo.add_transaction(tx)

    cursor = db_connection.cursor()
    cursor.execute("SELECT amount, type, category, description, date FROM transactions")
    result = cursor.fetchone()

    assert result == (
        tx.amount,
        tx.type,
        tx.category,
        tx.description,
        tx.date
    )

def test_get_all_transactions_returns_correct_objects(db_connection):
    repo = TransactionRepository(db_connection)
    data = copy.deepcopy(base_data)
    tx1 = Transaction(**data)
    tx2 = Transaction(
        amount=1200.00,
        type="income",
        category="Salary",
        description="June paycheck",
        date="2025-06-30"
    )
    repo.add_transaction(tx1)
    repo.add_transaction(tx2)

    transactions = repo.get_all_transactions()

    assert len(transactions) == 2
    assert isinstance(transactions[0], Transaction)
    assert transactions[0].amount == tx1.amount
    assert transactions[0].category == tx1.category
    assert transactions[1].type == tx2.type
    assert transactions[1].description == tx2.description
    assert transactions[1].date == tx2.date

