import sqlalchemy as sa
from .db_session import ORMBase
from sqlalchemy_serializer import SerializerMixin


class Jobs(ORMBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    team_leader = sa.Column(sa.Integer)
    job = sa.Column(sa.String)
    work_size = sa.Column(sa.Integer)
    collaborators = sa.Column(sa.String)
    is_finished = sa.Column(sa.Boolean)
