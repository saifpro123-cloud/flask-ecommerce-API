from flask import Flask
from app.config import Config
from app.extensions import db, jwt

from app.users.routes import users
from app.categories.routes import categories
from app.products.routes import products
from app.cart.routes import cart
from app.orders.routes import orders


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

        
    app.register_blueprint(users)
    app.register_blueprint(categories)
    app.register_blueprint(products)
    app.register_blueprint(cart)
    app.register_blueprint(orders)

      
    return app