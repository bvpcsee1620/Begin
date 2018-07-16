from app import db

class Role(db.Model):
    """ Staff Roles
    """
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '%r' % self.name

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.name == other

    def __key(self):
        return '%r%r' % (self.id,self.name)

    def __hash__(self):
        return hash(self.__key())