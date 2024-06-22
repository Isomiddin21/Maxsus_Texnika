from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum


from pydantic import BaseModel
from sqlalchemy import (
    Table, Column, Integer, String,
    Text, MetaData, Boolean, TIMESTAMP,
    Date, Enum, ForeignKey, DECIMAL,
    UniqueConstraint, Float
)



Base = declarative_base()
metadata = MetaData()
#
# blog = Table(
#     'blog',
#     metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('title', String(length=150), nullable=False),
#     Column('description', Text),
#     Column('created_date', TIMESTAMP, default=datetime.utcnow),
#     Column('is_active', Boolean, default=True),
#     Column('view_count', Integer, default=0)
# )
#
# userdata = Table(
#     'userdata',
#     metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('first_name', String, nullable=True),
#     Column('last_name', String, nullable=True),
#     Column('email', String),
#     Column('phone', String),
#     Column('username', String),
#     Column('password', String),
#     Column('birth_date', Date),
#     Column('registered_date', TIMESTAMP, default=datetime.utcnow)
# )



# class City(Base):
#     __tablename__ = 'city'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     country = Column(Integer, ForeignKey('country.id'))
#
#
# class Village(Base):
#     __tablename__ = 'village'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     village_id = Column(Integer, ForeignKey('city.id'))
#     city_id = Column(Integer, ForeignKey('city.id'))
#
#
# class Adress(Base):
#     __tablename__ = 'address'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     city = Column(Integer, ForeignKey('city.id'))
#     village = Column(Integer, ForeignKey('city.id'))
#     country = Column(Integer, ForeignKey('country.id'))
#
#
#
#
# class Category(Base):
#     __tablename__ = 'category'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#
#
# class Subcategory(Base):
#     __tablename__ = 'subcategory'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     category_id = Column(Integer, ForeignKey('category.id'))
#     category = relationship("Category")
#     UniqueConstraint('name', 'category_id', name='uniqNS')
#
#
#
#
#
#
# class Car(Base):
#     __tablename__ = 'car'
#     metadata = metadata
#     id = Column(Integer, primary_key=True)
#     type_id = Column(Integer, ForeignKey('brand.id'))
#     name = Column(String)
#     price = Column(DECIMAL(precision=10, scale=2))
#     quantity = Column(Integer)
#     created_at = Column(TIMESTAMP, default=datetime.uctnow)
#     description = Column(Text)
#     category_id = Column(Integer, ForeignKey, ('category.id'))
#     subcategory = Column(Integer, ForeignKey('subcategory.id'))
#
#
#
#
# class carsize(Base):
#     __tablename__ = 'carsize'
#     metadata = metadata
#     id = Column(Integer(primary_key=True, autoincrement=True))
#     car_id = Column(Integer, ForeignKey('car.id'))
#     size_id = Column(Integer, ForeignKey('size.id'))
#
#
#
#
# class Discount(Base):
#     __tablename__ = 'discount'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String)
#     discount = Column(Integer)
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)
#     start_date = Column(Date)
#     end_date = Column(Date)
#
#
# class Cardiscount(Base):
#     __tablename__ = 'cardiscount'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     car_id = Column(Integer, ForeignKey('carw.id'))
#     discount_id = Column(Integer, ForeignKey('discount.id'))
#
#
# class PaymentMethod(Base):
#     __tablename__ = 'paymentmethod'
#     cash = 'cash'
#     card = 'card'
#
#
#
#
#
#
#
# class File(Base):
#     __tablename__ = 'file'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     file = Column(String)
#     product_id = Column(Integer, ForeignKey('product.id'))
#     hash = Column(String, unique=True)
#
#
# class StatusEnum(enum.Enum):
#     Finding_car = 'finding_car'
#     processing = 'processing'
#     complated = 'complated'
#     canceled = 'canceled'
#
#
#
#
# class Order(Base):
#     __tablename__ = 'order'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     car_number = Column(Text)
#     user_id = Column(Integer, ForeignKey(userdata.id))
#     ordered_at = Column(TIMESTAMP, default=datetime.utcnow)
#     status = Column(Enum(PaymentMethod))
#     user_card_id = Column(Integer, ForeignKey('user_card.id'), nullable=True)
#
#
#
#
#
#
#
#
# class Order(Base):
#     __tablename__ = 'order'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     traking_number = Column(Text)
#     user_id = Column(Integer, ForeignKey(userdata.id))
#     ordered_at = Column(TIMESTAMP, default=datetime.utcnow)
#     status = Column(Enum(StatusEnum))
#     payment_method = Column(Enum())
#     shipping_addres_id = Column(Integer, ForeignKey('shipping_address_id'))
#     user_card_id = Column(Integer, ForeignKey)
#
#
#
# class Delivery(Base):
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     delevery_location = Column(String(255), nullable=False)
#     delivery_price = Column(DECIMAL(precision=10, scale=2))
#
#
#
#
#
#
#
#
#
#
# class CarOrder(BaseModel):
#     __tablename__ = 'car_order'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     color_id = Column(Integer, ForeignKey('color.id'))
#     size_id = Column(Integer, ForeignKey('size.id'))
#     car_id = Column(Integer, Integer, ForeignKey('car.id'))
#     order_id = Column(Integer, ForeignKey('order_id'))
#
#
#
#
#
#
#
# class UserCard(Base):
#     __tablename__ = 'user_card'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     card_number = Column(String)
#     card_expiration = Column(String)
#     cvc = Column(Integer)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     UniqueConstraint('card_number', 'user_id')
#
#
#
# class WishlistCard(Base):
#     __tablename__ = 'wishlist'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincement=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     car_id = Column(Integer, ForeignKey('car.id'))
#
#
#
#
#
# class Review(Base):
#     __tablename__ = 'review'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     message = Column(Text)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
#     product_id = Column(Integer, ForeignKey('product.id'))
#     star = Column(DECIMAL(precision=10, scale=1))
#     reviewed_at = Column(TIMESTAMP, default=datetime.utcnow)
#
#
#
#
# class Image(Base):
#     __tablename__ = 'images'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     image = Column(String)
#     product = Column(Integer, ForeignKey('product.id'))
#
#
# class ShoppingCart(Base):
#     __tablename__ = 'shopping_cart'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     product_id = Column(Integer, ForeignKey('product.id'))
#     count = Column(Integer, default=1)
#     added_at = Column(TIMESTAMP, default=datetime.utcnow)
#
#
#
# class Like(Base):
#     __tablename__ = 'like'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     product_id = Column(Integer, ForeignKey('product.id'))
#
#
#
#
# class Comment(Base):
#     __tablename__ = 'comment'
#     metadata = metadata
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer)
#     product_id = Column(Integer)
#     datatime = Column(TIMESTAMP, default=datetime.uctnow)
#
#
#
#
#
# class views(Base):
#     __tablename__ = 'views'
#     metadata = metadata
#     product_id = Column(Integer, ForeignKey('product.id'))
#     user_id = Column(Integer)
#     datetime = Column(TIMESTAMP, default=datetime.uctnow)
#
#
# class viewcount(Base):
#     __tablename__ = 'viewcount'
#     metadata = metadata
#
