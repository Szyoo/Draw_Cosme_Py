# database.session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base  # 导入 Base

DATABASE_URL = "sqlite:///./test.db"  # SQLite database file

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
