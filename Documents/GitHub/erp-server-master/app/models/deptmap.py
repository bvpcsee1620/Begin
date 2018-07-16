from app import db


class DeptMap(db.Model):
    __tablename__ = 'depts'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    dept_id = db.Column(db.Integer(), db.ForeignKey('department.id', ondelete='CASCADE'))