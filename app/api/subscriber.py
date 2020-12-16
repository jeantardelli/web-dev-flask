from . import api
from ..models import Subscriber 
from flask import jsonify, request, current_app, url_for

@api.route('/subscribers/<int:id>')
def get_subscriber(id):
    subscriber = Subscriber.query.get_or_404(id)
    return jsonify(subscriber.to_json())

@api.route('/subscribers/')
def get_subscibers():
    subscribers = Subscriber.query.all()
    return jsonify({'subscribers': [s.to_json() for s in subscribers]})
