from app import db


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String())
    first_name = db.Column(db.String())

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def __repr__(self):
        return '<id {}>'.format(self.id)
