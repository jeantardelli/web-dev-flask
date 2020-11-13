from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField

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
