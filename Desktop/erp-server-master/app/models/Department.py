from app import db
from app.models import User


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    hod_user_id = db.Column(db.Integer())                                                       # Hod Id
    department = db.Column(db.String(100),unique=True)                                            # Dept name

    def __init__(self,name):
        self.department = name

    def assign_hod(self, hod):
        self.hod_user_id = hod

    def __repr__(self):
        return "{}".format(self.department)

    def __str__(self):
        return self.__repr__()

    def json(self):
        return {
            "id": self.id,
            "hod_id": self.hod_user_id,
            "dept": self.department
        }