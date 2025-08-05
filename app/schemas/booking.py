from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class BookingBase(BaseModel):
    user_id: UUID
    screening_id: UUID
    num_tickets: int
    status: str


class BookingCreate(BookingBase):
    pass


class BookingRead(BookingBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
