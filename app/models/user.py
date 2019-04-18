import datetime
import math

from sqlalchemy import Sequence
from .base import Serializer, db


class User(db.Model, Serializer):
    __table__name = 'user'

    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def read(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    def update(self):
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, user_id):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
