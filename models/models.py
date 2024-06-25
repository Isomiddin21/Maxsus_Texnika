from datetime import datetime

from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Text,
    MetaData,
    Boolean,
    TIMESTAMP,
    Date, ForeignKey, Float
)
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

metadata = MetaData()
Base = declarative_base()


class Region(Base):
    __tablename__ = 'region'
    metadata = metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    region = Column(String)

    district = relationship('District', back_populates='region')
    driver = relationship('Driver', back_populates='region')


class District(Base):
    __tablename__ = 'district'
    metadata = metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    district = Column(String)
    region_id = Column(Integer, ForeignKey('region.id'))

    region = relationship('Region', back_populates='district')
    driver = relationship('Driver', back_populates='district')


class Driver(Base):
    __tablename__ = 'driver'
    metadata = metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    region_id = Column(Integer, ForeignKey('region.id'),nullable=True)
    district_id = Column(Integer, ForeignKey("district.id"), nullable=True)
    register_at = Column(TIMESTAMP, default=datetime.utcnow)

    region = relationship('Region', back_populates='driver')
    district = relationship('District', back_populates='driver')
    announcement = relationship('Announcement', back_populates='driver')


class Cars(Base):
    __tablename__ = 'cars'
    metadata = metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    services = relationship('Services', back_populates='cars')
    announcement = relationship('Announcement', back_populates='cars')


class Services(Base):
    __tablename__ = 'services'
    metadata = metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    car_id = Column(Integer, ForeignKey('cars.id'))

    cars = relationship('Services', back_populates='services')


class Announcement(Base):
    __tablename__ = 'announcement'
    metadata = metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    driver_id = Column(Integer, ForeignKey('driver.id'))
    max_price = Column(Float)
    min_price = Column(Float)
    description = Column(String)
    added_at = Column(Date, default=datetime.utcnow)
    is_active = Column(Boolean)

    @validates('min_price')
    def validate_min_price(self, key, value):
        if value < 10000:
            raise ValueError("min_price should be at least 10000")
        return value

    driver = relationship('Driver', back_populates='announcement')
    cars = relationship('Cars', back_populates='announcement')
    announcement_service = relationship('Announcement_service', back_populates='announcement')


class Announcement_service(Base):
    __tablename__ = 'announcement_service'
    metadata = metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    announcement_id = Column(Integer, ForeignKey('announcement.id'))
    service_id = Column(Integer, ForeignKey('services.id'))

    announcement = relationship('Announcement', back_populates='announcement_service')
    services = relationship('Services', back_populates='announcement_service')


