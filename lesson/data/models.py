import sqlalchemy as sa
import datetime
from sqlalchemy import orm
from .db_session import ORMBase


class User(ORMBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    about = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)

    news = orm.relation("News", back_populates='user')


class News(ORMBase):
    __tablename__ = 'news'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=True)
    content = sa.Column(sa.String, nullable=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    is_private = sa.Column(sa.Boolean, default=True)

    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    user = orm.relation('User')
