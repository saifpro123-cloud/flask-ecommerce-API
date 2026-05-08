from marshmallow import Schema, fields, validate

class CartItemSchema(Schema):

    product_id = fields.Integer(required=True)

    quantity = fields.Integer(required=True,validate=validate.Range(min=1))