# routes/health.py
from flask import Blueprint, jsonify
from services import health_service

bp = Blueprint('health', __name__, url_prefix='/health')

@bp.route('/', methods=['GET'])
def health_check():
    return jsonify(health_service.get_health_status())