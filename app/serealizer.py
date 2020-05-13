# -*- coding: utf-8 -*-
from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import Person, User

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person

    person = fields.Str(required=True)
    email = fields.Str(required=True)

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Não envie pelo amor de deus o ID')


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    username = fields.Str(required=True)
    password = fields.Str(required=True)
