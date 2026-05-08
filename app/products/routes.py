from flask import Blueprint, request
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extensions import db
from .models import Product
from .schema import ProductSchema
from app.categories.models import Category
from app.users.models import User

products = Blueprint("products", __name__)

@products.route("/product", methods=["POST"])
@jwt_required()
def create_product():
    user = User.query.get(get_jwt_identity())

    if not user or not user.is_admin:
        return {"success": False, "message": "Unauthorized"}, 403

    try:
        data = ProductSchema().load(request.get_json())
    except ValidationError as err:
        return {"success": False, "errors": err.messages}, 400

    category = Category.query.get(data["category_id"])
    if not category:
        return {"success": False, "message": "Category not found"}, 404

    product = Product(name=data["name"], description=data["description"], price=data["price"], stock=data["stock"], category_id=data["category_id"])

    db.session.add(product)
    db.session.commit()

    return {
        "success": True,
        "data": ProductSchema().dump(product)
    }, 201

@products.route("/product", methods=["GET"])
def get_products():
    products_list = Product.query.all()

    data = ProductSchema(many=True).dump(products_list)

    return {
        "success": True,
        "data": data
    }


@products.route("/product<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return {"success": False, "message": "Not found"}, 404

    return {
        "success": True,
        "data": ProductSchema().dump(product)
    }

@products.route("/product<int:product_id>", methods=["PUT"])
@jwt_required()
def update_product(product_id):
    user = User.query.get(get_jwt_identity())

    if not user or not user.is_admin:
        return {"success": False, "message": "Unauthorized"}, 403

    product = Product.query.get(product_id)
    if not product:
        return {"success": False, "message": "Not found"}, 404

    try:
        data = ProductSchema().load(request.get_json())
    except ValidationError as err:
        return {"success": False, "errors": err.messages}, 400

    
    for key, value in data.items():
        setattr(product, key, value)

    db.session.commit()

    return {
        "success": True,
        "data": ProductSchema().dump(product)
    }



@products.route("/product<int:product_id>", methods=["DELETE"])
@jwt_required()
def delete_product(product_id):
    user = User.query.get(get_jwt_identity())

    if not user or not user.is_admin:
        return {"success": False, "message": "Unauthorized"}, 403

    product = Product.query.get(product_id)
    if not product:
        return {"success": False, "message": "Not found"}, 404

    db.session.delete(product)
    db.session.commit()

    return {
        "success": True,
        "message": "Deleted"
    }