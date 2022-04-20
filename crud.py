from typing import List
from sqlalchemy.orm import Session
from exceptions import UserInfoAlreadyExistError, UserInfoNotFoundError
from models import UserInfo, GetUserInfo
from schemas import CreateAndUpdateUser, DeleteUser


# Method to get list of user info
def get_all_users(session: Session, limit: int, offset: int) -> List[UserInfo]:
    return session.query(GetUserInfo).filter(GetUserInfo.is_deleted == 0).offset(offset).limit(limit).all()


# Method to  get info of a particular user
def get_user_info_by_id(session: Session, user_id: int) -> UserInfo:
    user_info = session.query(GetUserInfo).filter_by(user_id=user_id, is_deleted=0).first()

    if user_info is None:
        raise UserInfoNotFoundError

    return user_info


# Method to add a new user info to the database
def create_user(session: Session, user_info: CreateAndUpdateUser) -> UserInfo:
    user_details = session.query(GetUserInfo).filter(GetUserInfo.email == user_info.email).first()
    if user_details is not None:
        raise UserInfoAlreadyExistError

    new_user_info = UserInfo(**user_info.dict())
    session.add(new_user_info)
    session.commit()
    session.refresh(new_user_info)
    return new_user_info


# Method to update details of the user
def update_user_info(
    session: Session, user_id: int, info_update: CreateAndUpdateUser) -> UserInfo:
    user_info = get_user_info_by_id(session, user_id)

    if user_info is None:
        raise UserInfoNotFoundError

    user_info.first_name = info_update.first_name
    user_info.last_name = info_update.last_name
    user_info.email = info_update.email
    user_info.city = info_update.city

    session.commit()
    session.refresh(user_info)

    return user_info


# Method to delete a user info from the table
def delete_user_info(session: Session, user_id: int) -> DeleteUser:
    user_info = get_user_info_by_id(session, user_id)

    if user_info is None:
        raise UserInfoNotFoundError

    # for soft delete
    user_info.is_deleted = 1

    # for hard delete
    # session.delete(user_info)
    
    session.commit()

    return {"msg": "User deleted successfully"}
