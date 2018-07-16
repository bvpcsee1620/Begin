from app import db
from app.models import User
from datetime import datetime,date

class FacultyAttendance(db.Model):
    __tablename__ = 'facultyattendance'
    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, unique=True)
    user_id = db.Column(db.Integer())
    date = db.Column(db.Date(),nullable=False)
    enter_time = db.Column(db.Time(), nullable=False)
    leave_time = db.Column(db.Time(), nullable=True)

    def __init__(self,user_id, date, et):
        self.user_id = user_id
        self.date = date
        self.enter_time = et

    def duration(self):
        if self.leave_time is None:
            return 0.00
        return (datetime.combine(date.today(), self.leave_time) - datetime.combine(date.today(), self.enter_time)).total_seconds()/60
