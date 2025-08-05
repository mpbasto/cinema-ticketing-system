from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class MovieBase(BaseModel):
    title: str
    description: str
    duration: int
    rating: str


class MovieCreate(MovieBase):
    pass


class MovieRead(MovieBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
