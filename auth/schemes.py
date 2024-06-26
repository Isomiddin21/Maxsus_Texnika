from datetime import datetime, date

from pydantic import BaseModel


class Sms_send(BaseModel):
    phone: str

class Sms_check(BaseModel):
    phone: str
    code:str
