from flask import Blueprint, request
from marshmallow import ValidationError

from app.extensions import db
from .models import Category
from .schema import CategorySchema

categories = Blueprint("categories", __name__)


@categories.route("/category", methods=["POST"])
def create_category():
    try:
        data = CategorySchema().load(request.get_json())
    except ValidationError as err:
        return {"success": False, "errors": err.messages}, 400

    if Category.query.filter_by(name=data["name"]).first():
        return {"success": False, "message": "Exists"}, 400

    category = Category(name=data["name"])

    db.session.add(category)
    db.session.commit()

    return {"success": True}


@categories.route("/category", methods=["GET"])
def get_categories():
    categories_list = Category.query.all()
    data = CategorySchema(many=True).dump(categories_list)

    return {"success": True, "data": data}