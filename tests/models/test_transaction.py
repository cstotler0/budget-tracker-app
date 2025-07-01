import copy
import pytest
from budget_tracker.models.transaction import Transaction

base_data = {
        "amount": 25.50,
        "type": "expense",
        "category": "Food",
        "date": "2025-06-30",
        "description": "Lunch"
}

def test_create_valid_transaction():
    data = copy.deepcopy(base_data)

    tx = Transaction(**data)

    assert tx.amount == 25.50
    assert tx.type == "expense"
    assert tx.category == "Food"
    assert tx.description == "Lunch"
    assert tx.date == "2025-06-30"

def test_negative_amount():
    data = copy.deepcopy(base_data)
    data["amount"] = -10.00

    with pytest.raises(ValueError) as exc_info:
        Transaction(**data)

    assert "Amount must be positive." in str(exc_info.value)

def test_invalid_type():
    data = copy.deepcopy(base_data)
    data ["type"] = "spending"

    with pytest.raises(ValueError) as exc_info:
        Transaction(**data)

    assert "Type must be either 'income' or 'expense'." in str(exc_info.value)

def test_optional_description():
    data = copy.deepcopy(base_data)
    del data["description"]

    tx = Transaction(**data)

    assert tx.description == ""

def test_empty_category():
    data = copy.deepcopy(base_data)
    data ["category"] = ""

    with pytest.raises(ValueError) as exc_info:
        Transaction(**data)

    assert "Category cannot be empty." in str(exc_info.value)