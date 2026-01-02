# 💰 Expense Tracker Web Application

## 📝 Short Description
A full-stack web application designed to help users track their daily expenses with ease, built using Python, Flask, and SQLAlchemy.

## 📖 Overview
The **Expense Tracker** is a robust, web-based tool aimed at simplifying personal finance management. It allows users to record, view, update, and delete expense records in a user-friendly interface. This project demonstrates the implementation of a full CRUD (Create, Read, Update, Delete) system within a **Model-View-Controller (MVC)** architecture, ensuring code maintainability and scalability.

## ✨ Features
*   **Add Expenses:** quickly log new expenses with details like title, description, category, amount, and date.
*   **View Dashboard:** Retrieve a comprehensive list of all recorded expenses.
*   **Edit Records:** Update existing expense details to correct errors or add information.
*   **Delete Entries:** Remove outdated or incorrect records from the database.
*   **Responsive Design:** Clean and accessible user interface styled with custom CSS.
*   **Data Persistence:** Reliable data storage using a SQLite database.

## 🛠️ Tech Stack
*   **Backend:** Python 3, Flask (Micro-framework), SQLAlchemy (ORM)
*   **Frontend:** HTML5, Jinja2 Templating Engine, CSS3
*   **Database:** SQLite
*   **Testing:** pytest

## 🏗️ Architecture
This project adheres to the **MVC (Model-View-Controller)** architectural pattern:

*   **Model (`models.py`):** Defines the data structure. The `Expense` class represents the database table, handling data validation and business logic.
*   **View (`templates/`):** Handles the presentation layer. HTML templates render the user interface, dynamically displaying data provided by the controller using Jinja2.
*   **Controller (`app.py`):** Manages the application flow. It processes incoming requests, interacts with the Model to fetch or update data, and selects the appropriate View to render the response.

## 📂 Project Structure
```
EXPENSE_TRACKER_APPLICATION/
├── app.py              # Application entry point and route definitions (Controller)
├── database.py         # Database connection and session management
├── models.py           # Database models definition (Model)
├── requirements.txt    # Python dependencies
├── static/
│   └── css/
│       └── style.css   # Custom stylesheets
├── templates/          # HTML Templates (View)
│   ├── add.html
│   ├── base.html
│   ├── dashboard.html
│   ├── edit.html
│   └── index.html
└── tests/              # Unit and integration tests
    ├── conftest.py
    ├── test_app.py
    └── test_models.py
```

## 🗄️ Database Design
The application uses a relational SQLite database. The primary entity is the **Expense** model:

| Column Name   | Data Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Primary Key, Unique Identifier |
| `title` | String | Title of the expense |
| `description` | String | Optional details about the expense |
| `category` | String | Category (e.g., Food, Transport) |
| `amount` | Float | Cost of the expense |
| `spent_on` | Date | Date the expense occurred |
| `created_at` | DateTime | Timestamp of record creation |
| `updated_at` | DateTime | Timestamp of last update |

## 🚀 Getting Started

### Prerequisites
*   Python 3.x installed on your system.
*   Git (optional, for cloning).

### Installation

1.  **Clone the repository (or download source):**
    ```bash
    git clone <repository-url>
    cd EXPENSE_TRACKER_APPLICATION
    ```

2.  **Set up a Virtual Environment (Recommended):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the Flask server:**
    ```bash
    python app.py
    ```
    *The database will be initialized automatically upon the first run.*

2.  **Access the App:**
    Open your web browser and navigate to:
    `http://127.0.0.1:5000`

## 🧪 Running Tests
To ensure the application is functioning correctly, you can run the test suite using `pytest`.

```bash
pytest
```

## 🔮 Future Enhancements
*   User Authentication (Login/Register).
*   Data visualization charts for monthly spending.
*   Export data to CSV/PDF.
*   Budget setting and alert features.

## 📄 License
This project is open-source and available for educational and personal use.
