from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class UserdataBase(BaseModel):
    status: str
    account: str
    user_name: str
    region: str
    time_zone: str
    music_account: str
    device_count: str

class Userdata(UserdataBase):
    class Config():
        orm_mode = True

class UpdateAccountBase(BaseModel):
    old_account: str
    new_account: str
    verification_code: str

class UpdateAccount(UpdateAccountBase):
    class Config():
        orm_mode = True

class UpdateRegionTimezoneBase(BaseModel):
    account: str
    region: str
    time_zone: str

class UpdateRegionTimezone(UpdateRegionTimezoneBase):
    class Config():
        orm_mode = True

class DevicedataBase(BaseModel):
    device_id: str
    account: str
    device_name: str
    language: str
    system_volume: int
    media_volume: int
    user_account: str

class Devicedata(DevicedataBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    #blogs: List[Blog] = []

    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True

class ShowUserdata(BaseModel):
    account: str
    user_name: str

    class Config():
        orm_mode = True

class ShowDevicedata(BaseModel):
    id: str
    device_name : str
    #creator: ShowUserdata

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None