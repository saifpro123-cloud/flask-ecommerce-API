
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extensions import db

from .models import Order, OrderItem

from app.cart.models import CartItem
from app.products.models import Product


orders = Blueprint("orders", __name__)

@orders.route("/checkout", methods=["POST"])
@jwt_required()
def checkout():

    user_id = get_jwt_identity()

    cart_items = CartItem.query.filter_by(
        user_id=user_id
    ).all()

    if not cart_items:
        return {
            "success": False,
            "message": "Cart is empty"
        }, 400

    order = Order(user_id=user_id)

    db.session.add(order)
    db.session.flush()

    for item in cart_items:

        product = Product.query.get(item.product_id)

        if product.stock < item.quantity:
            return {
                "success": False,
                "message": f"{product.name} out of stock"
            }, 400

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=item.quantity,
            price=product.price
        )

        db.session.add(order_item)

        product.stock -= item.quantity

        db.session.delete(item)

    db.session.commit()

    return {
        "success": True,
        "message": "Checkout completed",
        "order_id": order.id
    }, 201