from marshmallow import Schema, fields, validate

class RegisterSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2))

    email = fields.Email(required=True)

    password = fields.String(required=True, validate=validate.Length(min=6))

    is_admin = fields.Boolean()


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)