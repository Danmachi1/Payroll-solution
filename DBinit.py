import sqlite3

def init_db():
    conn = sqlite3.connect("payroll.db")
    cursor = conn.cursor()

    # Employees Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            account_number TEXT NOT NULL,
            hire_date TEXT,
            position TEXT,
            tax_rate REAL NOT NULL DEFAULT 10.0
        )
    """)

    # Jobs Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_name TEXT NOT NULL,
            rate_per_hour REAL NOT NULL
        )
    """)

    # Work Logs Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            job_id INTEGER NOT NULL,
            work_date TEXT NOT NULL,
            hours_worked REAL NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees (id),
            FOREIGN KEY (job_id) REFERENCES jobs (id)
        )
    """)

    # Payroll Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payroll (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            pay_period_start TEXT NOT NULL,
            pay_period_end TEXT NOT NULL,
            gross_pay REAL NOT NULL,
            total_deductions REAL NOT NULL,
            net_pay REAL NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    """)

    # Deductions Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS deductions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            is_percentage BOOLEAN NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    """)

    # Bonuses Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bonuses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    """)

    # Expenses Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            expense_date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending',
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    """)

    # Managers Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS managers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT NOT NULL DEFAULT 'Manager'
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

# Initialize the database
if __name__ == "__main__":
    init_db()
