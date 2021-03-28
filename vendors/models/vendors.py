from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from ..database.base import Base


class Vendors(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    external_link = Column(String)
    category = Column(String)
    status = Column(String)
    risk = Column(String)
    tier = Column(String)
