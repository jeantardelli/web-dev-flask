from . import db
from datetime import datetime
from flask import url_for
from app.exceptions import ValidationError

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<Subscriber %r>' % self.email

    def to_json(self):
        json_subscriber = {
            'url': url_for('api.get_subscriber', id=self.id),
            'email': self.email,
            }
        return json_subscriber

    def from_json(json_subscriber):
        email = json_subscriber.get('email')
        if email is None:
            raise ValidationError('subscriber does not have an email')
        return Subscriber(email)

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

    def to_json(self):
        json_letter = {
            'url': url_for('api.get_letter', id=self.id),
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'subject': self.subject,
            'body': self.body,
            'timestamp': self.timestamp
        }
        return json_letter

    def from_json(json_letter):
        firstname = json_letter.get('firstname')
        if firstname is None or firstname == '':
            raise ValidationError('letter does not have a firstname')
        if lastname is None or lastname == '':
            raise ValidationError('letter does not have a lastname')
        if email is None or email == '':
            raise ValidationError('letter does not have an email')
        if subject.lower() not in {'outro', 'heiki', 'tarot', 'massagem'}:
            raise ValidationError('subject is invalid')
        if body in None or body == '':
            raise ValidationError('letter does not have a body')
        return Letter(firstname, lastname, email, subject, body)
