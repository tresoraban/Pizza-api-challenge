from flask import Blueprint, jsonify
from server.models import Pizza

bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')

@bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])