from sqlalchemy import Column, Integer, Sequence, String

from app.common.database import Base


class User(Base):
    __table__name = 'user'

    uid = Column('id', Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, user_id, user_name):
        self.uid = user_id
        self.name = user_name

    @classmethod
    def read(cls, uid):
        return cls.query \
            .filter(User.uid == uid) \
            .first()

    @classmethod
    def read_list(cls):
        return cls.query \
            .order_by(User.name) \
            .all()
