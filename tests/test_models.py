from models import Expense
from datetime import date
import pytest
from sqlalchemy.exc import IntegrityError, StatementError
from database import db_session

def test_create_expense():
    """Test creating a new expense."""
    expense = Expense(
        title="Test Expense",
        description="This is a test expense.",
        category="Food",
        amount=10.50,
        spent_on=date(2025, 11, 13)
    )
    assert expense.title == "Test Expense"
    assert expense.description == "This is a test expense."
    assert expense.category == "Food"
    assert expense.amount == 10.50
    assert expense.spent_on == date(2025, 11, 13)

def test_create_expense_with_missing_title(app):
    """Test that creating an expense with a missing title raises an error."""
    with app.app_context():
        with pytest.raises(IntegrityError):
            expense = Expense(
                description="This is a test expense.",
                category="Food",
                amount=10.50,
                spent_on=date(2025, 11, 13)
            )
            db_session.add(expense)
            db_session.commit()

def test_create_expense_with_invalid_amount(app):
    """Test that the amount field rejects invalid data types."""
    with app.app_context():
        with pytest.raises(StatementError):
            expense = Expense(
                title="Test Expense",
                description="This is a test expense.",
                category="Food",
                amount="invalid",
                spent_on=date(2025, 11, 13)
            )
            db_session.add(expense)
            db_session.commit()
