from datetime import datetime, date

from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    password1: str
    password2: str
    birth_date: date


class UserInDB(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    password: str
    birth_date: date
    registered_date: datetime


class UserInfo(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    birth_date: date


class UserLogin(BaseModel):
    username: str
    password: str