from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


class AdminBase(BaseModel):
    email: EmailStr


class AdminCreate(AdminBase):
    password: str


class AdminRead(AdminBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
