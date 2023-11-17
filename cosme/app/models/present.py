# models.present.py

from app.database.base import Base
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

# Pydantic Model


class PresentBase(BaseModel):
    link: str
    present_name: str
    brand_name: str
    img_link: str

# SQLAlchemy Model


class Present(Base):
    __tablename__ = "presents"

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    present_name = Column(String)
    brand_name = Column(String)
    discovered_date = Column(DateTime, default=datetime.utcnow)
    img_link = Column(String)

    user_presents = relationship("UserPresent", back_populates="present")
