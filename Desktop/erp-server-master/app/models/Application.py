from app import db
from sqlalchemy.orm import validates
import re
from datetime import datetime
# TODO: Department validation
# TODO: ADD rejection Reason


class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    type = db.Column(db.String(3), nullable=False)
    c_email = db.Column(db.String(255), nullable=False)      # creator email
    c_name = db.Column(db.String(40))
    r_email = db.Column(db.String(255), nullable=True)       # replacement email
    department_id = db.Column(db.Integer(), db.ForeignKey('department.id'))
    message = db.Column(db.String(255), nullable=False)
    currentApprover = db.Column(db.String(255), nullable=False)
    isApprovedByReplacement = db.Column(db.Boolean(), default=False)
    c_date = db.Column(db.DateTime(), default=None)
    date_AR = db.Column(db.DateTime(), default=None)
    isApprovedByHod = db.Column(db.Boolean(), default=False)
    date_AH = db.Column(db.DateTime(), default=None)
    isApprovedByPrinicipal = db.Column(db.Boolean(), default=False)
    date_AP = db.Column(db.DateTime(), default=None)
    isRejected = db.Column(db.Boolean(), default=False)
    isApproved = db.Column(db.Boolean(), default=False)
    date_approved = db.Column(db.DateTime(), default=None)
    rejected_by = db.Column(db.String(255))                   # email of rejectent
    rejected_by_role = db.Column(db.String(50))
    date_rejected = db.Column(db.DateTime(), default=None)

    def __init__(self,type, c, r, m, c_approver, c_name, department_id):
        self.type = type
        self.c_email = c
        self.r_email = r
        self.message = m
        self.currentApprover = c_approver
        self.c_name = c_name
        self.c_date = datetime.now()
        self.department_id = department_id

    def json(self, profile_photo):
        return {
            "id": self.id,
            "c_name": self.c_name,
            "c_email": self.c_email,
            "c_date":self.c_date.strftime('%Y-%m-%d'),
            "type":self.type,
            "profile_photo": profile_photo,
            "r_email": self.r_email,
            "department": self.department_id,
            "message": self.message,
            "Replacement_Status": self.isApprovedByReplacement,
            "HOD_Status": self.isApprovedByHod,
            "Principal_Status": self.isApprovedByPrinicipal,
            "rejected_by": self.rejected_by,
            "current_approver": self.currentApprover,
            "is_rejected": self.isRejected,
            "rejected_by_role": self.rejected_by_role
        }

    def getStatusid(self):
        if self.isApproved is True:
            return 4
        elif self.isApprovedByHod is True:
            return 2
        elif self.isApprovedByReplacement is True:
            return 1
        else:
            return 0

    def applicationStatusJson(self):
        return {
            "id": self.id,
            "c_name": self.c_name,
            "type":self.type,
            "created_date":self.c_date,
            "Replacement_Status": self.isApprovedByReplacement,
            "HOD_Status": self.isApprovedByHod,
            "Principal_Status": self.isApprovedByPrinicipal,
            "rejected_by": self.rejected_by,
            "current_approver": self.currentApprover,
            "is_rejected": self.isRejected,
            "status_id":self.getStatusid(),
            "rejected_by_role": self.rejected_by_role,
            "is_approved": self.isApproved,
            "reject_date": self.date_rejected,
            "approved_date": self.date_approved,
            "message": self.message
        }

    @validates('c_email', 'r_email', 'rejected_by', 'currentApprover')
    def validate_email(self, key, email):
        if key in ['c_email', 'r_email'] and not email:
            raise AssertionError('No email provided')

        if key is 'rejected_by' and not email:
            return email

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not valid')

        return email