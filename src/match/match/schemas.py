from marshmallow import Schema, fields


class MatchSchema(Schema):
	idPlayer1 = fields.Integer(required=True)
	idPlayer2 = fields.Integer(required=True)
	scorePlayer1 = fields.Integer(required=True)
	scorePlayer2 = fields.Integer(required=True)
	result = fields.Integer(required=True, default=0)