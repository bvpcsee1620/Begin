from app import db
from sqlalchemy.orm import validates
import re


class SocketClient(db.Model):
    __tablename__ = 'socketclient'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    sid = db.Column(db.String(32))
    email = db.Column(db.String(255), nullable=False)

    def __init__(self, sid, email):
        self.sid = sid
        self.email = email

    def json(self):
        return {
            "id": self.id,
            "sid": self.sid,
            "email": self.email
        }

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not valid')

        return email