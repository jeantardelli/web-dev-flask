import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'mysql+mysqlconnector://pyuser:Py@pp4Demo@localhost:3306/sqlalchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Subscriber %r>' % self.email

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(64))
    subject = db.Column(db.String(64))
    body = db.Column(db.Text)

    def __repr__(self):
        return "<Message(firstname='{0}', lastname='{1}', email='{2}', "\
               "subject='{3}', body='{4}')>".format(self.firstname, self.lastname,
                self.email, self.subject, self.body)

class SubscribeForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Registrar')

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    firstname = StringField('First Name', validators=[DataRequired(), Length(1, 64)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(1, 64)])
    body = TextAreaField('Escreva sua mensagem', validators=[DataRequired()]) 
    subject = SelectField('Assunto', choices=['', 'Tarot', 'Massagem', 
        'Heiki', 'Outro'], validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Message=Message, Subscriber=Subscriber)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubscribeForm()
    if form.validate_on_submit():
        subscriber = Subscriber.query.filter_by(email=form.email.data).first()
        if subscriber is None:
            subscriber = Subscriber(email=form.email.data)
            db.session.add(subscriber)
            db.session.commit()
            flash('Obrigado! Seu email foi enviado com sucesso. Em breve você receberá novas informações.')
        else:
            flash('Este email já está registrado! ')
        session['email'] = form.email.data
        return redirect(url_for('index', _anchor='signup'))
    return render_template('index.html', form=form, email=session.get('email'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        subject = form.subject.data
        body = form.body.data
        message = Message(firstname=firstname, lastname=lastname, 
                          email=email, subject=subject, body=body)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('contact.html', form=form)
