import sqlite3

DB_NAME = "employees.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            department TEXT,
            position TEXT,
            salary REAL,
            is_test INTEGER DEFAULT 0
        )
    """)
    conn.close()


def save_employee(emp_id, full_name, department, position, salary):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        INSERT OR REPLACE INTO employees (id, full_name, department, position, salary, is_test)
        VALUES (?, ?, ?, ?, ?, 0)
    """, (emp_id, full_name, department, position, salary))
    conn.commit()
    conn.close()


def delete_employee(emp_id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    conn.close()


def get_all_employees():
    conn = sqlite3.connect(DB_NAME)
    rows = conn.execute("SELECT * FROM employees").fetchall()
    conn.close()
    return rows


def add_test_employees(employees):
    conn = sqlite3.connect(DB_NAME)
    conn.executemany(
        "INSERT INTO employees VALUES (?, ?, ?, ?, ?, 1)", employees
    )
    conn.commit()
    conn.close()


def delete_test_employees():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("DELETE FROM employees WHERE is_test=1")
    conn.commit()
    conn.close()
