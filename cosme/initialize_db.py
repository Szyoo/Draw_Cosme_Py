# initialize_db.py
# 初始化数据库

from sqlalchemy import create_engine
from app.database.base import Base
from app.models import user, present, user_present  # 从模型文件中导入所有模型

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database initialized!")
