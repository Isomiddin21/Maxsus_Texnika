import math
import os
import random
import secrets
import jwt
from datetime import datetime, timedelta

from auth.schemes import Sms_send, Sms_check
from auth.utils import generate_token
from models.models import Driver
from database import get_async_session
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
import redis
import math
import random
# from .utils import generate_token, verify_token

register_router = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# Connect to the Redis server
redis_client = redis.Redis(host='localhost', port=6379, db=0)


def generate_code(phone):
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def save_code(phone, code, ttl=60):
    key = f"phone:{phone}"
    redis_client.setex(key, ttl, code)


def check_code(phone, code):
    key = f"phone:{phone}"
    stored_code = redis_client.get(key)
    if stored_code is None:
        return False
    return stored_code.decode('utf-8') == code


@register_router.post('/sms-send')
async def send_sms(model: Sms_send):
    phone_number = model.phone
    generated_code = generate_code(phone_number)
    print(generated_code)
    save_code(phone_number, generated_code, 60)
    return {"detail": "SMS sent"}


@register_router.post('/check_sms')
async def check_sms(model: Sms_check, session: AsyncSession = Depends(get_async_session)):
    if check_code(model.phone, model.code):
        query = select(Driver).where(Driver.phone == model.phone)
        res = await session.execute(query)
        result = res.scalar_one_or_none()
        if result:
            token = generate_token(result.id)
            return {"token": token}
        else:
            raise HTTPException(status_code=404, detail="Driver not found")
    else:
        raise HTTPException(status_code=400, detail="Invalid code")


# # Main program
# a = input("Enter phone: ")
# code = generate_code(a)
# print(f"Generated code: {code}")
# save_code(a, code, 60)
# check = input("Enter verification code: ")
# if check_code(a, check):
#     print("Verified✅")
# else:
#     print("Incorrect code")
