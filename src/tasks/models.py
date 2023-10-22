from sqlalchemy import Integer, String, Text, Column, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
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
    title = Column(
        String(100),
        unique=True,
    )
    date_post = Column(
        DateTime,
    )
    date_update = Column(
        DateTime,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('')
    )
