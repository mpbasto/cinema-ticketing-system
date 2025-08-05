from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from app.core.db import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(Text, unique=True, nullable=False)
    description = Column(Text)
    duration = Column(Text, nullable=False)
    rating = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
