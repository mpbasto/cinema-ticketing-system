from datetime import datetime, timezone
import uuid
from sqlalchemy import UUID, Column, DateTime, Text

from app.core.db import Base


class Admin(Base):
    __tablename__ = "admins"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(Text, nullable=False)
    password_hash = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
