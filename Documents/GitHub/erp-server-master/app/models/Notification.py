from app import db
from sqlalchemy.orm import validates
import re


class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    s_email = db.Column(db.String(255), nullable=False)
    r_email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    s_profile_url =  db.Column(db.String(500), default="http://www.bvcoend.ac.in/")

    def __init__(self, sender, receiver, message,profile_url):
        self.s_email = sender
        self.r_email = receiver
        self.message = message
        self.s_profile_url = profile_url

    def json(self):
        return {
            "id": self.id,
            "sender_email": self.s_email,
            "receivers_email": self.r_email,
            "message": self.message,
            "s_profile_url": self.s_profile_url
        }

    @validates('s_email', 'r_email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not valid')

        return email

    @validates('s_profile_photo_url')
    def validate_email(self, key, url):
        if not url:
            raise AssertionError('No photo url provided')

        if not re.match("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", url):
            raise AssertionError('Provided photo url is not valid')

        return url
