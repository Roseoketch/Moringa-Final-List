from . import db


class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    cohort = db.Column(db.String(128), nullable=False, unique=False)
    ip_scores = db.Column(db.String(128), nullable=False)

    def __init__(self, id, name, cohort, ip_scores):

        self.id = id
        self.name = name
        self.cohort = cohort
        self.ip_scores = ip_scores

    def save_grade(self):
        db.session.add(self)
        db.session.commit()