from datetime import date

from sqlalchemy import func, select

from app.core.extensions import db
from app.models.queue import Queue

from .base_repository import BaseRepository
from app.core.enums import QueueStatus


class QueueRepository(BaseRepository):

    model = Queue

    @classmethod
    def get_last_queue_number(
        cls,
        shop_id,
        queue_date: date,
    ) -> int:

        stmt = select(
            func.max(Queue.queue_number)
        ).where(
            Queue.shop_id == shop_id,
            Queue.queue_date == queue_date,
        )

        result = db.session.scalar(stmt)

        return result or 0
      
    @classmethod
    def get_current_queue(
        cls,
        shop_id,
        queue_date,
    ):

        stmt = (
            select(Queue)
            .where(
                Queue.shop_id == shop_id,
                Queue.queue_date == queue_date,
                Queue.status == QueueStatus.SERVING.value,
            )
        )

        return db.session.scalar(stmt)
      
    @classmethod
    def get_last_queue(
        cls,
        shop_id,
        queue_date,
    ):

        stmt = (
            select(Queue)
            .where(
                Queue.shop_id == shop_id,
                Queue.queue_date == queue_date,
            )
            .order_by(Queue.queue_number.desc())
        )

        return db.session.scalar(stmt)
      
    @classmethod
    def get_next_waiting(
        cls,
        shop_id,
        queue_date,
    ):

        stmt = (
            select(Queue)
            .where(
                Queue.shop_id == shop_id,
                Queue.queue_date == queue_date,
                Queue.status == QueueStatus.WAITING.value,
            )
            .order_by(Queue.queue_number.asc())
        )

        return db.session.scalar(stmt)
    
    @classmethod
    def get_waiting_queue(
        cls,
        shop_id,
        queue_date,
    ):

        stmt = (
            select(Queue)
            .where(
                Queue.shop_id == shop_id,
                Queue.queue_date == queue_date,
                Queue.status == QueueStatus.WAITING.value,
            )
            .order_by(Queue.queue_number.asc())
        )

        return db.session.scalar(stmt)