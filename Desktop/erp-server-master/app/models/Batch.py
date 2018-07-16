from app import db
from sqlalchemy.orm import validates


class Batch(db.Model):
    __tablename__ = 'batch'
    id = db.Column(db.Integer(), primary_key=True)
    # email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            # "email": self.email,
            "name": self.name
        }

    @validates('name')
    def validate_username(self, key, name):
        if not name:
            raise AssertionError('No batch provided')

        if len(name) < 1 or len(name) > 10:
            raise AssertionError('Batch name must be between 1 and 10 characters')

        return name