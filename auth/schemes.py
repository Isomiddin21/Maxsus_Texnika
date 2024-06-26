from datetime import datetime, date
from typing import List

from pydantic import BaseModel


class Sms_send(BaseModel):
    phone: str


class Sms_check(BaseModel):
    phone: str
    code: str


class Driver_register(BaseModel):
    first_name: str
    last_name: str
    phone: str
    region_id: int
    district_id: int


class Get_regions(BaseModel):
    id:int
    region:str

class Get_districts(BaseModel):
    id:int
    district:str
    region_id:Get_regions




class Add_car_service(BaseModel):
    car_id:int
    names:List[str]


class Add_announcement(BaseModel):
    car_id:int
    max_price:float
    min_price:float
    description:str
    service_id:List[int]