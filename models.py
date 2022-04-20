from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer

from database import Base


class UserInfo(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    city = Column(String)


class GetUserInfo(UserInfo):
    is_deleted = Column(Integer)
