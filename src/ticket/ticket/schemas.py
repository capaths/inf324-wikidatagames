from marshmallow import Schema, fields


class TicketSchema(Schema):
    id = fields.Integer()
    title = fields.Str()
    description = fields.Integer()
