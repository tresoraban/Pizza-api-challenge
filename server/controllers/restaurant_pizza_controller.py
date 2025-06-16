from flask import Blueprint, jsonify, request
from server.models import RestaurantPizza, db
from server import db

bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    # Validate required fields
    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required_fields):
        return jsonify({'errors': ['Missing required fields']}), 400

    # Validate price range
    price = data['price']
    if not 1 <= price <= 30:
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    try:
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400