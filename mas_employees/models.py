"""Data models."""
from . import db
from faker import Faker
from sqlalchemy import event

import random
from random import randint

class Employee(db.Model):
    """Data model for Employees accounts."""

    __tablename__ = "mas-employess-employee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    salary = db.Column(db.Integer, index=False, unique=False, nullable=False)
    salary_type = db.Column(db.String(64), index=False, unique=False, nullable=True)

    def __repr__(self):
        return "<Employee {}>".format(self.name)


@event.listens_for(Employee.__table__, "after_create")
def create_employees(*args, **kwargs):
    fake = Faker()
    for _ in range(10):
        new_employee = Employee(
            name=fake.name(),
            email=fake.email(),
            salary=randint(10000, 50000),
            salary_type=random.choice(["Monthly", "Hourly"]),
        )
        db.session.add(new_employee)  # Adds new User record to database
        db.session.commit()  # Commits all changes