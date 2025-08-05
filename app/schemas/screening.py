from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ScreeningBase(BaseModel):
    movie_id: UUID
    screening_time: datetime
    location: str
    total_seats: int
    available_seats: int


class ScreeningCreate(ScreeningBase):
    pass


class ScreeningRead(ScreeningBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
