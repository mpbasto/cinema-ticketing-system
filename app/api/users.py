from datetime import datetime, timezone
from uuid import UUID, uuid4
import bcrypt
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.core.db import get_db

router = APIRouter()


@router.get("/", response_model=List[UserRead])
async def read_users(
    skip: int = 0, limit: Optional[int] = None, db: AsyncSession = Depends(get_db)
):
    query = select(User).offset(skip)
    if limit is not None:
        query = query.limit(limit)
    result = await db.execute(query)
    users = result.scalars().all()
    return users


@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user_in.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = bcrypt.hashpw(
        user_in.password.encode(), bcrypt.gensalt()
    ).decode()

    new_user = User(
        email=user_in.email, password_hash=hashed_password, name=user_in.name
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user
