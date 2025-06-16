from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from server.controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller
    app.register_blueprint(restaurant_controller.bp)
    app.register_blueprint(pizza_controller.bp)
    app.register_blueprint(restaurant_pizza_controller.bp)

    return app