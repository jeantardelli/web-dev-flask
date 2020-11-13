from . import db
from datetime import datetime

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<Subscriber %r>' % self.email

class Letter(db.Model):
    __tablename__ = 'letters'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(64), index=True)
    subject = db.Column(db.String(64))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Letter(firstname='{0}', lastname='{1}', email='{2}', "\
               "subject='{3}', body='{4}')>".format(self.firstname, self.lastname,
                self.email, self.subject, self.body)
