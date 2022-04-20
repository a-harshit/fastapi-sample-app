from typing import List, Optional

from pydantic import BaseModel


# POST and PUT APIs
class CreateAndUpdateUser(BaseModel):
    first_name: str
    last_name: str
    city: str
    email: str


# GET API
class User(CreateAndUpdateUser):
    user_id: int

    class Config:
        orm_mode = True


# List users API
class PaginatedUserInfo(BaseModel):
    limit: int
    offset: int
    data: List[User]


# DELETE API
class DeleteUser():
    msg: str
