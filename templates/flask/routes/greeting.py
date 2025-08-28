# routes/greeting.py
from flask import Blueprint, jsonify
import os
from controllers import greeting_controller

bp = Blueprint('greeting', __name__, url_prefix='/greeting')

@bp.route('/', methods=['GET'])
def get_greeting():
    username = os.getenv("USER", "Usuário")
    return jsonify(greeting_controller.handle_greeting(username))

@bp.route('/<name>', methods=['GET'])
def get_personalized_greeting(name):
    return jsonify(greeting_controller.handle_greeting(name))