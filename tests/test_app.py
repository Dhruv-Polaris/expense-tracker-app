from models import Expense
from datetime import datetime

def test_index(client):
    """Test that the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Expenses" in response.data

def test_add_expense(client):
    """Test that a new expense can be added."""
    response = client.post('/add', data={
        'title': 'Test Expense',
        'description': 'This is a test expense.',
        'category': 'Food',
        'amount': '10.50',
        'spent_on': '2025-11-13'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Expense" in response.data
    assert b"10.50" in response.data

    expense = Expense.query.first()
    assert expense.title == 'Test Expense'
    assert expense.amount == 10.50

def test_edit_expense(client):
    """Test that an expense can be edited."""
    # First, add an expense to edit
    client.post('/add', data={
        'title': 'Test Expense',
        'description': 'This is a test expense.',
        'category': 'Food',
        'amount': '10.50',
        'spent_on': '2025-11-13'
    }, follow_redirects=True)

    expense = Expense.query.first()
    response = client.post(f'/edit/{expense.id}', data={
        'title': 'Updated Expense',
        'description': 'This is an updated expense.',
        'category': 'Travel',
        'amount': '25.00',
        'spent_on': '2025-11-14'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Updated Expense" in response.data
    assert b"25.00" in response.data

    updated_expense = Expense.query.get(expense.id)
    assert updated_expense.title == 'Updated Expense'
    assert updated_expense.category == 'Travel'
    assert updated_expense.amount == 25.00

def test_delete_expense(client):
    """Test that an expense can be deleted."""
    # First, add an expense to delete
    client.post('/add', data={
        'title': 'Test Expense',
        'description': 'This is a test expense.',
        'category': 'Food',
        'amount': '10.50',
        'spent_on': '2025-11-13'
    }, follow_redirects=True)

    expense = Expense.query.first()
    response = client.post(f'/delete/{expense.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Expense" not in response.data

    deleted_expense = Expense.query.get(expense.id)
    assert deleted_expense is None
