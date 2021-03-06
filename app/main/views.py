from .. import db
from ..models import Subscriber, Letter
from ..email import send_email
from . import main_bp
from .forms import SubscribeForm, ContactForm
from flask import render_template, session, redirect, url_for, current_app, flash
from flask_sqlalchemy import get_debug_queries

@main_bp.after_app_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= current_app.config['APP_SLOW_DB_QUERY_TIME']:
            current_app.logger.warning(
                    'Slow query: {0}\nParameters: {1}\nDuration: {2}\nContext: '
                    '{3}\n'.format(query.statement, query.parameters,
                                   query.duration, query.context))
    return response

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = SubscribeForm()
    if form.validate_on_submit():
        subscriber = Subscriber.query.filter_by(email=form.email.data).first()
        if subscriber is None:
            subscriber = Subscriber(email=form.email.data)
            db.session.add(subscriber)
            db.session.commit()
            flash("Obrigado! Seu email foi enviado com sucesso. "
                  "Em breve você receberá novas informações.")
            if current_app.config['APP_ADMIN']:
                send_email(current_app.config['MAIL_SENDER'], 'New Subscriber',
                        'mail/new_subscriber', subscriber=subscriber)
        else:
            flash('Este email já está registrado!')
        session['email'] = form.email.data
        return redirect(url_for('.index', _anchor='signup'))
    return render_template('index.html', form=form, email=session.get('email'))

@main_bp.route('/success')
def success():
    return render_template('success.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        subject = form.subject.data
        body = form.body.data
        letter = Letter(firstname=firstname, lastname=lastname,
                          email=email, subject=subject, body=body)
        db.session.add(letter)
        db.session.commit()
        if current_app.config['APP_ADMIN']:
            send_email(current_app.config['MAIL_SENDER'], 'New Message',
                    'mail/new_message', letter=letter)
        return redirect(url_for('.success'))
    return render_template('contact.html', form=form)
