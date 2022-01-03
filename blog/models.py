from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")

class Userdata(Base):
    __tablename__ = 'userdatas'

    id = Column(Integer, primary_key = True, index = True)
    status = Column(String)
    account = Column(String)
    user_name = Column(String)
    region = Column(String)
    time_zone = Column(String)
    music_account = Column(String)
    device_count = Column(String)

    devicedatas = relationship("Devicedata", back_populates="creator2")

class Devicedata(Base):
    __tablename__ = 'devicedatas'

    id = Column(Integer, primary_key = True, index = True)
    device_id = Column(String)
    account = Column(String)
    device_name = Column(String)
    language = Column(String)
    system_volume = Column(Integer)
    media_volume = Column(Integer)
    user_account = Column(Integer, ForeignKey('userdatas.account'))

    creator2 = relationship("Userdata", back_populates="devicedatas")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")