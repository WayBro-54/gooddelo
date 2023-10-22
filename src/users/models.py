from typing import Optional, List
from datetime import date
from sqlalchemy import (Integer, String, Text, Column, DateTime, Date)
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.core.db import Base
from src.base import Tasks

class Users(Base):
    __tablename__ = 'd_users'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    surname: Mapped[str] = mapped_column(
        String(100),
    )
    firstname: Mapped[str] = mapped_column(
        String(100),
    )
    lastname: Mapped[Optional[str]] = mapped_column(
        String(100),
    )
    birthdate: Mapped[date] = mapped_column(
        Date,
    )
    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
    )
    password = mapped_column(
        String(100),
    )
    date_register: Mapped[date]  = mapped_column(

    )
    tasks: Mapped[Optional[List[Tasks]]]  = relationship(
        back_populates='id'
    )