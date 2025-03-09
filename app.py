from flask import Flask, request, jsonify
import db_operations as db
from  db_operations import *


app = Flask(__name__)

# Create a new employee
@app.route("/employees", methods=["POST"])
def create_employee():
    data = request.json
    db.create_employee(
        data["name"], data["account_number"], data["hire_date"], data["position"], data["tax_rate"]
    )
    return jsonify({"message": "Employee created successfully!"}), 201

# Get all employees
@app.route("/employees", methods=["GET"])
def get_employees():
    employees = db.get_all_employees()
    return jsonify({"employees": employees})

# Get an employee by ID
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = db.get_employee_by_id(employee_id)
    if employee:
        return jsonify({"employee": employee})
    return jsonify({"message": "Employee not found"}), 404

# Update an employee
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    data = request.json
    db.update_employee(
        employee_id,
        data["name"], data["account_number"], data["hire_date"], data["position"], data["tax_rate"]
    )
    return jsonify({"message": "Employee updated successfully!"})
@app.route("/payroll/gross_pay", methods=["POST"])
def get_gross_pay():
    data = request.json
    employee_id = data["employee_id"]
    start_date = data["start_date"]
    end_date = data["end_date"]

    gross_pay = db.calculate_gross_pay(employee_id, start_date, end_date)
    return jsonify({"gross_pay": gross_pay})

@app.route("/payroll/calculate", methods=["POST"])
def calculate_payroll_route():
    data = request.json
    employee_id = data["employee_id"]
    start_date = data["start_date"]
    end_date = data["end_date"]

    payroll = db.calculate_payroll(employee_id, start_date, end_date)
    return jsonify(payroll)
@app.route("/jobs", methods=["POST"])
def create_job_route():
    data = request.json
    create_job(data["job_name"], data["rate_per_hour"])
    return jsonify({"message": "Job created successfully!"}), 201


@app.route("/work_logs", methods=["POST"])
def create_work_log_route():
    data = request.json
    create_work_log(data["employee_id"], data["job_id"], data["work_date"], data["hours_worked"])
    return jsonify({"message": "Work log created successfully!"}), 201


@app.route("/deductions", methods=["POST"])
def create_deduction_route():
    data = request.json
    create_deduction(data["employee_id"], data["type"], data["amount"], data["is_percentage"])
    return jsonify({"message": "Deduction created successfully!"}), 201


@app.route("/bonuses", methods=["POST"])
def create_bonus_route():
    data = request.json
    create_bonus(data["employee_id"], data["type"], data["amount"])
    return jsonify({"message": "Bonus created successfully!"}), 201


@app.route("/expenses", methods=["POST"])
def create_expense_route():
    data = request.json
    create_expense(data["employee_id"], data["expense_date"], data["description"], data["amount"], data["status"])
    return jsonify({"message": "Expense created successfully!"}), 201


# Delete an employee
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    db.delete_employee(employee_id)
    return jsonify({"message": "Employee deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
