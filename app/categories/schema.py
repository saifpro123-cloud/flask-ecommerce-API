from marshmallow import Schema, fields

class CategorySchema(Schema):
    name = fields.String(required=True)