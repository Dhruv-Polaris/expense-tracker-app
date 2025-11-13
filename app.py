from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, db_session
from models import Expense
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_expense = Expense(
            title=request.form['title'],
            description=request.form['description'],
            category=request.form['category'],
            amount=float(request.form['amount']),
            spent_on=datetime.strptime(request.form['spent_on'], '%Y-%m-%d').date()
        )
        db_session.add(new_expense)
        db_session.commit()
        flash('Expense added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    expense = Expense.query.get(id)
    if request.method == 'POST':
        expense.title = request.form['title']
        expense.description = request.form['description']
        expense.category = request.form['category']
        expense.amount = float(request.form['amount'])
        expense.spent_on = datetime.strptime(request.form['spent_on'], '%Y-%m-%d').date()
        db_session.commit()
        flash('Expense updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', expense=expense)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    expense = Expense.query.get(id)
    db_session.delete(expense)
    db_session.commit()
    flash('Expense deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
