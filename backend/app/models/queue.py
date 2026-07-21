from __future__ import annotations

import datetime
import uuid

from sqlalchemy import Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.extensions import db
from app.models.base import TimestampMixin, UUIDMixin
# from app.models.enums import QueueStatus
from app.core.enums import QueueStatus
from sqlalchemy import UniqueConstraint, Index


class Queue(db.Model, UUIDMixin, TimestampMixin):
    __tablename__ = "queues"
    
    __table_args__ = (
      Index(
          "ix_queue_shop_date",
          "shop_id",
          "queue_date",
      ),
    )

    shop_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("shops.id"),
        nullable=False,
    )

    queue_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    device_id: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
    )

    queue_date: Mapped[datetime.date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        # Enum(QueueStatus),
        String(20),
        default=QueueStatus.WAITING.value,
        nullable=False,
    )

    shop: Mapped["Shop"] = relationship(
        back_populates="queues",
    )