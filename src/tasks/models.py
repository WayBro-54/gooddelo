from sqlalchemy import Integer, String, Text, Column
from src.core.db import Base



class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
    )
    desriptions = Column(
        Text,
        nullable=False,
    )
