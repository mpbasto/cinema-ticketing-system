from datetime import datetime, timezone
import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from app.core.db import Base


class Screening(Base):
    __tablename__ = "screenings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    movie_id = Column(UUID(as_uuid=True), ForeignKey("movies.id", ondelete="CASCADE"))
    screening_time = Column(DateTime, nullable=False)
    location = Column(Text, nullable=False)
    total_seats = Column(Integer, nullable=False)
    available_seats = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    movie = relationship("Movie", backref="screenings")
