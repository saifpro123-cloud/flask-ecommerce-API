from flask import  Blueprint, request
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extensions import db

from .models import CartItem
from .schema import CartItemSchema

from app.products.models import Product
from app.users.models import User


cart=Blueprint("cart", __name__)


@cart.route("/cart", methods=["POST"])
@jwt_required()
def add_to_cart():

    user_id = get_jwt_identity()

    try:
        data = CartItemSchema().load(request.get_json())

    except ValidationError as err:
        return {
            "success": False,
            "errors": err.messages
        }, 400


    product = Product.query.get(data["product_id"])

    if not product:
        return {
            "success": False,
            "message": "Product not found"
        }, 404

    
    if product.stock < data["quantity"]:
        return {
            "success": False,
            "message": "Not enough stock"
        }, 400

    
    cart_item = CartItem.query.filter_by(
        user_id=user_id,
        product_id=data["product_id"]
    ).first()

    
    if cart_item:
        cart_item.quantity += data["quantity"]

    
    else:
        cart_item = CartItem(
            user_id=user_id,
            product_id=data["product_id"],
            quantity=data["quantity"]
        )

        db.session.add(cart_item)

    db.session.commit()

    return {
        "success": True,
        "message": "Added to cart"
    }, 201



@cart.route("/cart", methods=["GET"])
@jwt_required()
def get_cart():

    user_id = get_jwt_identity()

    cart_items = CartItem.query.filter_by(
        user_id=user_id
    ).all()

    data = []

    for item in cart_items:

        product = Product.query.get(item.product_id)

        data.append({
            "cart_item_id": item.id,
            "product_id": product.id,
            "product_name": product.name,
            "price": product.price,
            "quantity": item.quantity
        })

    return {
        "success": True,
        "data": data
    },200



@cart.route("/cart/<int:item_id>", methods=["DELETE"])
@jwt_required()
def remove_from_cart(item_id):

    user_id = get_jwt_identity()

    cart_item = CartItem.query.filter_by(
        id=item_id,
        user_id=user_id
    ).first()

    if not cart_item:
        return {
            "success": False,
            "message": "Item not found"
        },404

    db.session.delete(cart_item)

    db.session.commit()

    return {
        "success": True,
        "message": "Item removed"
    },200