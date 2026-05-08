from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from app.extensions import db
from .models import User
from .schema import RegisterSchema, LoginSchema

users = Blueprint("users", __name__)


@users.route("/register", methods=["POST"])
def register():
    try:
        data = RegisterSchema().load(request.get_json())
    except ValidationError as err:
        return {"success": False, "errors": err.messages}, 400

    if User.query.filter_by(email=data["email"]).first():
        return {"success": False, "message": "Email exists"}, 400

    user = User(
        name=data["name"],
        email=data["email"],
        password=generate_password_hash(data["password"])
    )

    db.session.add(user)
    db.session.commit()

    return {"success": True, "message": "User created"}, 201


@users.route("/login", methods=["POST"])
def login():
    try:
        data = LoginSchema().load(request.get_json())
    except ValidationError as err:
        return {"success": False, "errors": err.messages}, 400

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return {"success": False, "message": "Invalid data"}, 401

    token = create_access_token(identity=user.id)

    return {"success": True, "data": {"token": token}}