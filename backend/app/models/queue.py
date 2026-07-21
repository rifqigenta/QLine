from __future__ import annotations

import datetime
import uuid

from sqlalchemy import Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.extensions import db
from app.models.base import TimestampMixin, UUIDMixin
from app.models.enums import QueueStatus
from sqlalchemy import UniqueConstraint, Index


class Queue(db.Model, UUIDMixin, TimestampMixin):
    __tablename__ = "queues"
    
    __table_args__ = (
      UniqueConstraint(
          "shop_id",
          "device_id",
          "queue_date",
          name="uq_queue_device_per_day",
      ),
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

    device_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    queue_date: Mapped[datetime.date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[QueueStatus] = mapped_column(
        Enum(QueueStatus),
        default=QueueStatus.WAITING,
        nullable=False,
    )

    shop: Mapped["Shop"] = relationship(
        back_populates="queues",
    )