import sqlalchemy
from db_session import SqlAlchemyBase


class DataMsg(SqlAlchemyBase):
    __tablename__ = 'data'

    srv_id = sqlalchemy.Column(sqlalchemy.Integer,
                               primary_key=True, nullable=True)
    msg_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    i = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    end = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)