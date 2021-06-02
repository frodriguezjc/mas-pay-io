"""Product pages."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

from mas_employees.models import db, Employee

# Blueprint Configuration
employee_bp = Blueprint(
    "employees_bp", __name__, template_folder="templates", static_folder="static"
)


@employee_bp.route("/employees/<int:employee_id>/", methods=["GET"])
def employee_page(employee_id):
    """employee description page."""
    employee = Employee.query.filter_by(id=employee_id).first()
    return render_template(
        "employees.jinja2",
        employee=employee,
        template="profile-template",
    )
