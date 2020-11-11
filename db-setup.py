import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# Define the MySQL engine using MySQL Connector/Python
engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://pyuser:Py@pp4Demo@localhost:3306/sqlalchemy',
    echo=True)

# Define and create the table
Base = declarative_base()

class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    email = sqlalchemy.Column(sqlalchemy.String(64), unique=True)

    def __repr__(self):
        return "<Subscriber(email='{0}')>".format(self.email)

class Message(Base):
    __tablename__ = 'messages'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    firstname = sqlalchemy.Column(sqlalchemy.String(64))
    lastname = sqlalchemy.Column(sqlalchemy.String(64))
    email = sqlalchemy.Column(sqlalchemy.String(64))
    subject = sqlalchemy.Column(sqlalchemy.String(64))
    body = sqlalchemy.Column(sqlalchemy.Text)

    def __repr__(self):
        return "<Message(firstname='{0}', lastname='{1}', email='{2}', "\
               "subject='{3}', body='{4}')>".format(self.firstname, self.lastname,
                self.email, self.subject, self.body)

Base.metadata.create_all(engine)
