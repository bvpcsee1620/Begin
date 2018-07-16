from app import db
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates
from sqlalchemy import extract
import re
from .FacultyAttendance import FacultyAttendance
from .Application import Application
# TODO: google scholor papers, Department Validation
from datetime import datetime
import calendar


def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return [mylist.index(sub_list), sub_list.index(char)]
    raise ValueError("'{char}' is not in list".format(char=char))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(256), nullable=False)
    number = db.Column(db.VARCHAR(10), nullable=False)
    profile_photo_url = db.Column(db.String(
        500), default="https://ariellemcgill.files.wordpress.com/2018/03/unnamed.png")
    profile_url = db.Column(
        db.String(500), default="http://www.bvcoend.ac.in/")
    name = db.Column(db.String(30), nullable=False)
    subjects = db.Column(db.String(700), nullable=True, default=None)
    labs = db.Column(db.String(700), nullable=True, default=None)
    designation = db.Column(db.String(70), nullable=True, default=None)
    pass_reset = db.Column(db.Boolean(), default=False)
    prev_reset_token = db.Column(db.String(256), default=None)
    department_id = db.relationship('Department', secondary='depts')
    roles = db.relationship('Role', secondary='user_roles')

    def __init__(self, email, profile_photo_url, number, profile_url, name, subjects, designation, labs, prev_reset_token=None, pass_reset=False):
        self.username = email
        self.profile_photo_url = profile_photo_url
        self.number = number
        self.profile_url = profile_url
        self.name = name
        self.subjects = subjects
        self.designation = designation
        self.labs = labs
        self.email = email
        self.prev_reset_token = prev_reset_token
        self.pass_reset = pass_reset

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def has_roles(self, *roles):
        for role in roles:
            if role in self.roles:
                return True
        return False

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_auth_token(self, expiration=60000):
        s = Serializer('kufia', expires_in=expiration)
        return s.dumps({'id': self.id})

    def generate_reset_token(self, expiration=60*60*24):
        s = Serializer('kufiasecret', expires_in=expiration)
        return s.dumps({'id': self.id})

    def json(self):
        return {
            "email": self.username,
            "number": self.number,
            "profile_photo_url": self.profile_photo_url,
            "profile_url": self.profile_url,
            "name": self.name,
            "department": str(self.department_id),
            "roles": str(self.roles)
        }

    def profile_json(self,current_month = datetime.now().month,current_year = datetime.now().year):

        total_attendance_month = FacultyAttendance.query.filter(FacultyAttendance.user_id == self.id).filter(
            extract('month', FacultyAttendance.date) == current_month).all()

        total_attendance_month_durations = [
            a.duration() for a in total_attendance_month]
        total_duration_month = sum(total_attendance_month_durations)
        prev_m_a = FacultyAttendance.query.filter(FacultyAttendance.user_id == self.id).filter(
            extract('month', FacultyAttendance.date) == current_month - 1).all()
        prev_total = sum([a.duration() for a in prev_m_a])
        if prev_total == 0:
            percentage_change = 100
        else:
            percentage_change = (
                (total_duration_month - prev_total)/prev_total)*100
        Leaves_applications = Application.query.filter(Application.c_email == self.email).filter(Application.isApproved == True).filter(
            extract('month', Application.date_AP) == current_month).all()
        month_days = calendar.monthcalendar(current_year, current_month)
        duration_dict = {}
        for m in total_attendance_month:
            duration_dict[m.date.day] = m.duration()
        week_hours = [sum([duration_dict[day] if day in duration_dict else 0 for day in week])for i,week in enumerate(month_days)]
        current_week = find_in_list_of_list(month_days, datetime.now().day)
        return {
            "department": str(self.department_id[0]),
            "designation": self.designation,
            "month_total_mins": total_duration_month or 0,
            "leaves": len(Leaves_applications),
            "full_attendance": duration_dict,
            "month_days": month_days,
            "percentage_change": percentage_change,
            "current_week": current_week,
            "week_hours":week_hours
        }

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('kufia')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

    @staticmethod
    def verify_reset_token(token):
        s = Serializer('kufiasecret')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not valid')

        return email

    @validates('number')
    def validate_email(self, key, number):
        if not number:
            raise AssertionError('No number provided')

        if len(number) != 10:
            raise AssertionError('Provided mobile number is not valid')

        return number

    @validates('profile_url')
    def validate_email(self, key, url):
        if not url:
            raise AssertionError('No url provided')

        if not re.match("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", url):
            raise AssertionError('Provided url is not valid')

        return url

    @validates('profile_photo_url')
    def validate_email(self, key, url):
        if not url:
            raise AssertionError('No photo url provided')

        if not re.match("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", url):
            raise AssertionError('Provided photo url is not valid')

        return url
