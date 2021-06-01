"""General page routes."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

from mas_employees.api import fetch_products
from mas_employees.models import db, Employee

# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET"])
def home():
    """Homepage."""
    employees = Employee.query.all()
    return render_template(
        "index.jinja2",
        title="Welcome to pay-mas.io",
        subtitle="List Existing users.",
        template="home-template",
        mployees=employees
    )

@home_bp.route("/employees", methods=["GET"])
def employees():
    """List of Employees."""
    employees = Employee.query.all()
    return render_template(
        "index.jinja2",
        title="List Employees",
        subtitle="List Existing users.",
        template="home-template",
        employees=employees
    )

@home_bp.route("/about", methods=["GET"])
def about():
    """About page."""
    return render_template(
        "index.jinja2",
        title="About",
        subtitle="This is an example about page.",
        template="home-template page",
    )


@home_bp.route("/contact", methods=["GET"])
def contact():
    """Contact page."""
    return render_template(
        "index.jinja2",
        title="Contact",
        subtitle="This is an example contact page.",
        template="home-template page",
    )
