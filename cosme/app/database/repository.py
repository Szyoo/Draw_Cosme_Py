# database.repository.py

from sqlalchemy.orm import Session
from app.models.user import User
from app.models.present import Present
from app.models.user_present import UserPresent

# User CRUD操作


def create_user(db: Session, user: User) -> User:
    """
    创建一个新用户
    :param db: 数据库会话
    :param user: 用户对象
    :return: 创建的用户
    示例:
        user = User(name="John", email="john@example.com")
        with get_db() as db:
            create_user(db, new_user)
    """
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int) -> User:
    """
    根据用户ID获取用户
    :param db: 数据库会话
    :param user_id: 用户ID
    :return: 用户对象或None
    示例:
        with get_db() as db:
            user = get_user(db, 1)
    """
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, updated_user: User) -> User:
    """
    更新用户信息
    :param db: 数据库会话
    :param user_id: 要更新的用户ID
    :param updated_user: 更新的用户信息
    :return: 更新的用户或None
    示例:
        updated_user = User(name="Johnny", email="johnny@example.com")
        with get_db() as db:
            update_user(db, 1, updated_user)
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for key, value in updated_user.__dict__.items():
            setattr(db_user, key, value)
        db.commit()
        return db_user
    return None


def delete_user(db: Session, user_id: int) -> bool:
    """
    删除用户
    :param db: 数据库会话
    :param user_id: 要删除的用户ID
    :return: 是否删除成功
    示例:
        with get_db() as db:
            result = delete_user(db, 1)
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

# Present CRUD操作


def create_present(db: Session, present: Present) -> Present:
    """
    创建礼物
    :param db: 数据库会话
    :param present: 礼物对象
    :return: 创建的礼物
    示例:
        present = Present(name="Toy", description="Children's toy")
        with get_db() as db:
            create_present(db, present)
    """
    db.add(present)
    db.commit()
    db.refresh(present)
    return present


def get_present(db: Session, present_id: int) -> Present:
    """
    根据礼物ID获取礼物
    :param db: 数据库会话
    :param present_id: 礼物ID
    :return: 礼物对象或None
    示例:
        with get_db() as db:
            present = get_present(db, 1)
    """
    return db.query(Present).filter(Present.id == present_id).first()


def update_present(db: Session, present_id: int, updated_present: Present) -> Present:
    """
    更新礼物信息
    :param db: 数据库会话
    :param present_id: 要更新的礼物ID
    :param updated_present: 更新的礼物信息
    :return: 更新的礼物或None
    示例:
        updated_present = Present(name="Toy", description="Updated children's toy")
        with get_db() as db:
            update_present(db, 1, updated_present)
    """
    db_present = db.query(Present).filter(Present.id == present_id).first()
    if db_present:
        for key, value in updated_present.__dict__.items():
            setattr(db_present, key, value)
        db.commit()
        return db_present
    return None


def delete_present(db: Session, present_id: int) -> bool:
    """
    删除礼物
    :param db: 数据库会话
    :param present_id: 要删除的礼物ID
    :return: 是否删除成功
    示例:
        with get_db() as db:
            result = delete_present(db, 1)
    """
    db_present = db.query(Present).filter(Present.id == present_id).first()
    if db_present:
        db.delete(db_present)
        db.commit()
        return True
    return False

# UserPresent CRUD操作


def create_user_present(db: Session, user_present: UserPresent) -> UserPresent:
    """
    创建用户礼物关联
    :param db: 数据库会话
    :param user_present: 用户礼物关联对象
    :return: 创建的用户礼物关联
    示例:
        user_present = UserPresent(user_id=1, present_id=1)
        with get_db() as db:
            create_user_present(db, user_present)
    """
    db.add(user_present)
    db.commit()
    db.refresh(user_present)
    return user_present


def get_user_present(db: Session, user_present_id: int) -> UserPresent:
    """
    根据ID获取用户礼物关联
    :param db: 数据库会话
    :param user_present_id: 用户礼物关联ID
    :return: 用户礼物关联对象或None
    示例:
        with get_db() as db:
            user_present = get_user_present(db, 1)
    """
    return db.query(UserPresent).filter(UserPresent.id == user_present_id).first()


def update_user_present(db: Session, user_present_id: int, updated_user_present: UserPresent) -> UserPresent:
    """
    更新用户礼物关联
    :param db: 数据库会话
    :param user_present_id: 要更新的用户礼物关联ID
    :param updated_user_present: 更新的用户礼物关联信息
    :return: 更新的用户礼物关联或None
    示例:
        updated_user_present = UserPresent(user_id=1, present_id=2)
        with get_db() as db:
            update_user_present(db, 1, updated_user_present)
    """
    db_user_present = db.query(UserPresent).filter(
        UserPresent.id == user_present_id).first()
    if db_user_present:
        for key, value in updated_user_present.__dict__.items():
            setattr(db_user_present, key, value)
        db.commit()
        return db_user_present
    return None


def delete_user_present(db: Session, user_present_id: int) -> bool:
    """
    删除用户礼物关联
    :param db: 数据库会话
    :param user_present_id: 要删除的用户礼物关联ID
    :return: 是否删除成功
    示例:
        with get_db() as db:
            result = delete_user_present(db, 1)
    """
    db_user_present = db.query(UserPresent).filter(
        UserPresent.id == user_present_id).first()
    if db_user_present:
        db.delete(db_user_present)
        db.commit()
        return True
    return False


def get_presents_by_user(db: Session, user_id: int):
    """
    根据用户ID获取该用户的所有礼物的查询。
    :param db: 数据库会话
    :param user_id: 用户ID
    :return: 该用户的所有礼物的查询
    示例:
        with get_db() as db:
            presents_query = get_presents_by_user(db, 1)
            presents = presents_query.all()
    """
    return db.query(UserPresent).filter(UserPresent.user_id == user_id)


def count_presents_by_user(db: Session, user_id: int) -> int:
    """
    根据用户ID计算该用户的礼物总数。
    :param db: 数据库会话
    :param user_id: 用户ID
    :return: 用户的礼物总数
    示例:
        with get_db() as db:
            total_presents = count_presents_by_user(db, 1)
    """
    return db.query(UserPresent).filter(UserPresent.user_id == user_id).count()


def get_drawn_by_user(db: Session, user_id: int):
    """
    根据用户ID获取该用户已被抽中的所有礼物的查询。
    :param db: 数据库会话
    :param user_id: 用户ID
    :return: 该用户已被抽中的所有礼物的查询
    示例:
        with get_db() as db:
            drawn_presents_query = get_drawn_by_user(db, 1)
            drawn_presents = drawn_presents_query.all()
    """
    return db.query(UserPresent).filter(UserPresent.user_id == user_id, UserPresent.is_drawn == True)


def count_drawn_presents_by_user(db: Session, user_id: int) -> int:
    """
    根据用户ID计算该用户已被抽中的礼物总数。
    :param db: 数据库会话
    :param user_id: 用户ID
    :return: 用户已被抽中的礼物总数
    示例:
        with get_db() as db:
            total_drawn_presents = count_drawn_presents_by_user(db, 1)
    """
    return db.query(UserPresent).filter(UserPresent.user_id == user_id, UserPresent.is_drawn == True).count()
