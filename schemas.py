from pydantic import BaseModel, EmailStr
from datetime import datetime

class FitnessClassBase(BaseModel):
    name: str
    instructor: str
    date_time: datetime
    available_slots: int

class FitnessClassOut(FitnessClassBase):
    id: int
    class Config:
        from_attributes = True

class BookingBase(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BookingBase):
    id: int
    class Config:
        from_attributes = True

