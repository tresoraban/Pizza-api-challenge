from flask import Blueprint, jsonify, request
from server.models import Restaurant, RestaurantPizza, db

bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    pizzas = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
    response = restaurant.to_dict()
    response['pizzas'] = pizzas
    return jsonify(response)

@bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204