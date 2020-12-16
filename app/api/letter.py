from . import api
from ..models import Letter
from flask import jsonify, request, current_app, url_for

@api.route('/letters/<int:id>')
def get_letter(id):
    letter = Letter.query.get_or_404(id)
    return jsonify(letter.to_json())

@api.route('/letters/')
def get_letters():
    letters = Letter.query.all()
    return jsonify({'letters': [l.to_json() for l in letters]})
