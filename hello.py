from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

class SubscribeForm(FlaskForm):
    """ .. todo: write a method that validates if the email is already subscribed """
    email = EmailField('Email', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Inscreva-se')

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    firstname = StringField('First Name', validators=[DataRequired(), Length(1, 64)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(1, 64)])
    body = TextAreaField('Escreva sua mensagem', validators=[DataRequired()]) 
    subject = StringField('Assunto', validators=[DataRequired()])
    submit = SubmitField('Enviar')
                
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
        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('Obrigado! Seu email foi enviado com sucesso. Em breve você receberá novas informações.')
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
        body = form.body.data
        firstname = form.firstname.data
        lastname = form.lastname
        email = form.email.data
        subject = form.subject.data
        print(firstname, lastname, email, subject, body)
        return redirect(url_for('success'))
    return render_template('contact.html', form=form)
