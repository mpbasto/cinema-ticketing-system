from datetime import datetime, timezone
import uuid
from sqlalchemy import UUID, Column, DateTime, Enum, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.core.db import Base


class BookingStatusEnum(Enum):
    CONFIRMED = "CONFIRMED"
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    screening_id = Column(
        UUID(as_uuid=True), ForeignKey("screenings.id", ondelete="CASCADE")
    )
    num_tickets = Column(Integer, nullable=False)
    status = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    user = relationship("User", backref="bookings")
    screening = relationship("Screening", backref="bookings")
