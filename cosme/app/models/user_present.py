# models.user_present.py

from app.database.base import Base
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

# Pydantic Model


class UserPresentBase(BaseModel):
    user_id: int
    present_id: int
    draw_date: datetime
    is_drawn: bool

# SQLAlchemy Model


class UserPresent(Base):
    __tablename__ = "user_present"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    present_id = Column(Integer, ForeignKey('presents.id'))
    draw_date = Column(DateTime, default=datetime.utcnow)
    is_drawn = Column(Boolean, default=False)

    user = relationship("User", back_populates="user_presents")
    present = relationship("Present", back_populates="user_presents")
