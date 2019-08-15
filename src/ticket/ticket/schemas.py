from marshmallow import Schema, fields


class TicketSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Integer(required=True)
