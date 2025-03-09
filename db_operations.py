import sqlite3
from flask import Flask, request, jsonify

DB_FILE = "payroll.db"

# Function to connect to the database
def get_db_connection():
    return sqlite3.connect(DB_FILE)

# --- Employees CRUD ---
def create_employee(name, account_number, hire_date, position, tax_rate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees (name, account_number, hire_date, position, tax_rate)
        VALUES (?, ?, ?, ?, ?)
    """, (name, account_number, hire_date, position, tax_rate))
    conn.commit()
    conn.close()

# --- Jobs CRUD ---
def create_job(job_name, rate_per_hour):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jobs (job_name, rate_per_hour)
        VALUES (?, ?)
    """, (job_name, rate_per_hour))
    conn.commit()
    conn.close()

# --- Work Logs CRUD ---
def create_work_log(employee_id, job_id, work_date, hours_worked):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO work_logs (employee_id, job_id, work_date, hours_worked)
        VALUES (?, ?, ?, ?)
    """, (employee_id, job_id, work_date, hours_worked))
    conn.commit()
    conn.close()

# --- Payroll CRUD ---
def create_payroll(employee_id, pay_period_start, pay_period_end, gross_pay, total_deductions, net_pay):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO payroll (employee_id, pay_period_start, pay_period_end, gross_pay, total_deductions, net_pay)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (employee_id, pay_period_start, pay_period_end, gross_pay, total_deductions, net_pay))
    conn.commit()
    conn.close()

# --- Bonuses Integration ---
def calculate_total_bonuses(employee_id, start_date, end_date):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount) AS total_bonuses
        FROM bonuses
        WHERE employee_id = ?;
    """, (employee_id,))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result[0] else 0.0

# --- Expenses Integration ---
def calculate_total_expenses(employee_id, start_date, end_date):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount) AS total_expenses
        FROM expenses
        WHERE employee_id = ? AND status = 'Pending';
    """, (employee_id,))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result[0] else 0.0

# --- Payroll Calculation ---
def calculate_gross_pay(employee_id, start_date, end_date):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query to calculate gross pay
    cursor.execute("""
        SELECT SUM(w.hours_worked * j.rate_per_hour) AS gross_pay
        FROM work_logs w
        JOIN jobs j ON w.job_id = j.id
        WHERE w.employee_id = ? AND w.work_date BETWEEN ? AND ?;
    """, (employee_id, start_date, end_date))

    result = cursor.fetchone()
    conn.close()

    # Return gross pay (default to 0 if no records found)
    return result[0] if result[0] else 0.0

def calculate_total_deductions(employee_id, gross_pay):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all deductions for the employee
    cursor.execute("""
        SELECT amount, is_percentage
        FROM deductions
        WHERE employee_id = ?;
    """, (employee_id,))
    deductions = cursor.fetchall()
    conn.close()

    total_deductions = 0

    # Calculate total deductions
    for amount, is_percentage in deductions:
        if is_percentage:  # Percentage-based deduction
            total_deductions += (gross_pay * amount / 100)
        else:  # Fixed deduction
            total_deductions += amount

    return total_deductions

def calculate_payroll(employee_id, start_date, end_date):
    # Step 1: Calculate gross pay
    gross_pay = calculate_gross_pay(employee_id, start_date, end_date)

    # Step 2: Calculate total deductions
    total_deductions = calculate_total_deductions(employee_id, gross_pay)

    # Step 3: Calculate total bonuses
    total_bonuses = calculate_total_bonuses(employee_id, start_date, end_date)

    # Step 4: Calculate total expenses
    total_expenses = calculate_total_expenses(employee_id, start_date, end_date)

    # Step 5: Calculate net pay
    net_pay = gross_pay - total_deductions + total_bonuses - total_expenses

    return {
        "gross_pay": gross_pay,
        "total_deductions": total_deductions,
        "total_bonuses": total_bonuses,
        "total_expenses": total_expenses,
        "net_pay": net_pay
    }

# --- Save Payroll Record ---
def save_payroll_record(employee_id, start_date, end_date, gross_pay, total_deductions, total_bonuses, total_expenses, net_pay):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO payroll (employee_id, pay_period_start, pay_period_end, gross_pay, total_deductions, net_pay)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (employee_id, start_date, end_date, gross_pay, total_deductions, net_pay))

    conn.commit()
    conn.close()

# --- Flask App ---
app = Flask(__name__)

@app.route("/payroll/calculate", methods=["POST"])
def calculate_payroll_route():
    data = request.json
    employee_id = data["employee_id"]
    start_date = data["start_date"]
    end_date = data["end_date"]

    payroll = calculate_payroll(employee_id, start_date, end_date)

    # Save payroll record
    save_payroll_record(
        employee_id,
        start_date,
        end_date,
        payroll["gross_pay"],
        payroll["total_deductions"],
        payroll["total_bonuses"],
        payroll["total_expenses"],
        payroll["net_pay"]
    )

    return jsonify(payroll)

@app.route("/employees", methods=["POST"])
def create_employee_route():
    data = request.json
    create_employee(data["name"], data["account_number"], data["hire_date"], data["position"], data["tax_rate"])
    return jsonify({"message": "Employee created successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
