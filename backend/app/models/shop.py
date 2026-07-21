from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text

from app.models.base import TimestampMixin, UUIDMixin
from app.core.extensions import db

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from app.models.queue import Queue

class Shop(db.Model, UUIDMixin, TimestampMixin):
    __tablename__ = "shops"

    display_code: Mapped[str] = mapped_column(
        String(8),
        unique=True,
        nullable=False,
    )

    public_code: Mapped[str] = mapped_column(
        String(16),
        unique=True,
        nullable=False,
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
    Text,
    nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    is_open: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    
    queues: Mapped[list["Queue"]] = relationship(
    back_populates="shop",
    cascade="all, delete-orphan",
    )