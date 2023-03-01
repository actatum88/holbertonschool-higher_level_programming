from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base

"""Base Model"""

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
