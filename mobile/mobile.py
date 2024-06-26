import datetime
import secrets
from typing import List

import aiofiles
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi_pagination import Page, add_pagination, paginate
# from fastapi_pagination.ext.sqlalchemy import paginate

from sqlalchemy import select, insert, or_, and_, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from auth.utils import verify_token
from database import get_async_session
from datetime import datetime, timedelta

mobile_router = APIRouter()


# @mobile_router.post('/add_announcement')
# async def add_announcement(token)



