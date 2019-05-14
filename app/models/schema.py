from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow_sqlalchemy import ModelConverter

from .user import User

ma = Marshmallow()


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)
