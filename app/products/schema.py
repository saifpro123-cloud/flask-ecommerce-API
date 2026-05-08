from marshmallow import Schema, fields, validate

class ProductSchema(Schema):

    name = fields.String(required=True)
    description = fields.String()

    price = fields.Float(required=True, validate=validate.Range(min=0))
    stock = fields.Integer(required=True, validate=validate.Range(min=0))

    category_id = fields.Integer(required=True)

    