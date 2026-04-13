import sqlite3

DB_NAME = "employees.db"


def average_salary_by_department():
    conn = sqlite3.connect(DB_NAME)
    rows = conn.execute(
        "SELECT department, AVG(salary) FROM employees GROUP BY department"
    ).fetchall()
    conn.close()
    return rows