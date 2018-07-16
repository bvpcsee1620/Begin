from app import db
import datetime
from sqlalchemy.orm import validates
import re
from .User import User

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    s_email = db.Column(db.String(255), nullable=False)
    r_email = db.Column(db.String(255), nullable=False)
    task = db.Column(db.String(255), nullable=False)
    isDone = db.Column(db.BOOLEAN())
    recv_date = db.Column(db.String(255))
    to_complete_date = db.Column(db.String(255))
    s_profile_photo_url = db.Column(db.String(500), default="https://ariellemcgill.files.wordpress.com/2018/03/unnamed.png")

    def __init__(self, sender, receiver, task, complete_date, profile_url, recv_date=datetime.datetime.now()):
        self.s_email = sender
        self.s_profile_photo_url = profile_url
        self.r_email = receiver
        self.task = task
        self.isDone = False
        self.recv_date = recv_date
        self.to_complete_date = complete_date

    def json(self):
        sender = User.query.filter(User.email == self.s_email).first()
        return {
            "id": self.id,
            "sender_email": self.s_email,
            "receivers_email": self.r_email,
            "task": self.task,
            "data": {
                "s_name":sender.name,
                "s_email":self.s_email,
                "s_designation":sender.designation,
                "s_number":sender.number,
                "s_department":str(sender.department_id[0])
            },
            "to_complete_date": self.to_complete_date,
            "s_profile_url":self.s_profile_photo_url
        }

    @validates('s_email', 'r_email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not valid')

        return email

    @validates('recv_date', 'to_complete_date')
    def validate_email(self, key, date):
        if not date:
            raise AssertionError('No email provided')

        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise AssertionError('Provided date is not valid')

        return date

    @validates('s_profile_photo_url')
    def validate_email(self, key, url):
        if not url:
            raise AssertionError('No photo url provided')

        if not re.match("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", url):
            raise AssertionError('Provided photo url is not valid')

        return url


