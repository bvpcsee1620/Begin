from app import db
from sqlalchemy.orm import validates
import re


class Lectures(db.Model):
    __tablename__ = 'lectures'
    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, unique=True)
    t_name = db.Column(db.String(80), nullable=False)
    t_email = db.Column(db.String(80), nullable=False)
    lec_name = db.Column(db.String(80), nullable=False)
    room_id = db.Column(db.String(80), nullable=False)
    s = db.Column(db.DateTime(), nullable=False)
    e = db.Column(db.DateTime(), nullable=False)
    batch_name = db.Column(db.String(80), nullable=True)
    batch_part = db.Column(db.String(10), nullable=True)
    day = db.Column(db.String(80), nullable=False)

    def __init__(self, t_name, t_email, lec_name, room_id, start_time, end_time, day, batch_name, batch_part):
        self.t_name = t_name
        self.t_email = t_email
        self.lec_name = lec_name
        self.room_id = room_id
        self.s = start_time
        self.e = end_time
        self.day = day
        self.batch_name = batch_name
        self.batch_part = batch_part

    def info(self):
        return {
            "id": self.id,
            "t_name": self.t_name,
            "t_email": self.t_email,
            "batch": self.batch_name
        }

    def json(self):
        return{
            "id": self.id,
            "t_name": self.t_name,
            "t_email": self.t_email,
            "lec_name": self.lec_name,
            "room_id": self.room_id,
            "start_time": self.s,
            "end_time": self.e,
            "day": self.day,
            "batch_name": self.batch_name,
            "batch_part": self.batch_part
        }

    def to_task(self,date):
        return {
            "id": self.id,
            "sender_email": "bvcoe.erp@gmail.com",
            "receivers_email": self.t_email,
            "task": "Lecture at {} in {} of {} for batch {}".format(self.s.strftime("%I:%M %p"), self.room_id.upper(), self.lec_name.upper(), self.batch_name.upper()),
            "to_complete_date":date,
            "data": {
                "s_name":"ERP Bot",
                "s_email":"bvcoe.erp@gmail.com",
                "s_designation":"Content Provider",
                "s_number":"0000000000",
                "s_department":"CSE"
            },
            "s_profile_url":"https://vignette.wikia.nocookie.net/monstergirlencyclopedia/images/d/d0/Discord_logo.png/revision/latest?cb=20160622232221"
        }

    @validates('t_email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not valid')

        return email

    @validates('day')
    def validate_email(self, key, day):
        if not day:
            raise AssertionError('No day provided')

        if day.lower() not in ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]:
            raise AssertionError('Provided day is not valid')

        return day
