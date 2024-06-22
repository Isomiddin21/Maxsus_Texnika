from datetime import datetime, date
from pydantic import BaseModel


from datetime import datetime
from pydantic import BaseModel, Field, conint
from typing import Optional, List
from typing import Union

from pydantic import BaseModel, Field






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


class ShippingAddressScheme(BaseModel):
    shipping_address: str




class ShippingAddressGetScheme(BaseModel):
    id: int
    shipping_address: str
    user_id: int



class UserCardScheme(BaseModel):
    card_number:str = Field(max_length=16, min_length=16)
    card_expression: str = Field(maxlength=4, mini_length=4)
    card_cvc: Optional[int] = Field(None)


class CardSchemeSche(BaseModel):
    id: int
    card_number: int
    card_expression: int


class LikeScheme(BaseModel):
    id: int
    user_id: int




class WishListScheme(BaseModel):
    id: int
    cars: int


class Rewievscheme(BaseModel):
    id: int
    message: str
    user_id: int














# class ShoppingCartScheme(BaseModel):
#     product: dict
#     id: int
#     count: int
#     added_at: datetime
#
#
# class ShoppingSaveCartScheme(BaseModel):
#     product_id: int
#     count: Optional[conint(ge=0)]
#
#
# class ShippingAddressScheme(BaseModel):
#     shipping_address: str
#
#
# class ShippingAddressGetScheme(BaseModel):
#     id: int
#     shipping_address: str
#     user_id: int
#
#
# class UserCardScheme(BaseModel):
#     card_number: str = Field(max_length=16, min_length=16)
#     card_expiration: str = Field(max_length=4, min_length=4)
#     card_cvc: Optional[int] = None
#
#
# class CardScheme(BaseModel):
#     id: int
#     card_number: str
#     card_expiration: str
#
#
# class OrderSchema(BaseModel):
#     product_id: int
#     tracking_number: Optional[str]
#     status: str
#     payment_method: str
#     shipping_address_id: int
#     delivery_method_id: int
#     user_card_id: Optional[int]
# class ReviewCreate(BaseModel):
#     message: Union[str, None]
#     product_id: int
#     star: float
#
#
# class ReviewGet(BaseModel):
#     id: int
#     message: str
#     user_id: int
#     product_id: int
#     star: float
#
#
# class LikeScheme(BaseModel):
#     product_id: int
#
# class LikeGet(BaseModel):
#     id: int
#     user_id: int
#     product: int
#     description: str
#     title: str
#
#
# class WishlistScheme(BaseModel):
#     user_id: int
#     product_id: int
#
#
#
#
#























