# models.user.py

from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database.base import Base
from pydantic import BaseModel


class ProfessionEnum(PyEnum):
    EMPLOYEE = "会社員"
    PART_TIME = "パート・アルバイト"
    SELF_EMPLOYED = "自営業・自由業"
    HOUSEWIFE = "専業主婦"
    STUDENT = "学生"
    UNEMPLOYED = "仕事はしていない"

# Pydantic Model


class UserBase(BaseModel):
    email: str
    password: str
    name: str
    age: int
    profession: ProfessionEnum

    class Config:
        arbitrary_types_allowed = True

# SQLAlchemy Model


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    age = Column(Integer)
    profession = Column(
        Enum(*[e.value for e in ProfessionEnum]), default=ProfessionEnum.EMPLOYEE.value)

    user_presents = relationship("UserPresent", back_populates="user")
