from app.ext import db
"""
class Record:
    fname
    lname
    comment
"""

class Record(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    fname=db.Column(db.String(255))
    lname=db.Column(db.String(255))
    comment=db.Column(db.Text())

    def __repr__(self) -> str:
        return f"<Record for user {self.fname} {self.lname}>"