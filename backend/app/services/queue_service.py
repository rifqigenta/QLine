from datetime import date

from app.core.enums import QueueStatus
from app.exceptions.errors import NotFoundException
from app.repositories.queue_repository import QueueRepository
from app.repositories.shop_repository import ShopRepository


class QueueService:

    @staticmethod
    def take_queue(public_code: str):

        shop = ShopRepository.get_by_public_code(public_code)

        if shop is None:
            raise NotFoundException("Shop not found")

        today = date.today()

        last_number = QueueRepository.get_last_queue_number(
            shop.id,
            today,
        )

        queue = QueueRepository.create(
            shop_id=shop.id,
            queue_date=today,
            queue_number=last_number + 1,
            status=QueueStatus.WAITING.value,
        )

        QueueRepository.commit()

        return {
            "queue_number": queue.queue_number,
            "status": queue.status,
            "queue_date": str(queue.queue_date),
        }

    @staticmethod
    def get_status(public_code: str):

        shop = ShopRepository.get_by_public_code(public_code)

        if shop is None:
            raise NotFoundException("Shop not found")

        today = date.today()

        current = QueueRepository.get_current_queue(
            shop.id,
            today,
        )

        last = QueueRepository.get_last_queue(
            shop.id,
            today,
        )

        current_number = current.queue_number if current else None
        last_number = last.queue_number if last else 0
        remaining = (
            last_number - current_number
            if current_number is not None
            else last_number
        )

        return {
            "current_queue": current_number,
            "last_queue": last_number,
            "remaining": remaining,
        }

    @staticmethod
    def next_queue(public_code: str):

        shop = ShopRepository.get_by_public_code(public_code)

        if shop is None:
            raise NotFoundException("Shop not found")

        today = date.today()

        current = QueueRepository.get_current_queue(
            shop.id,
            today,
        )

        if current:
            current.status = QueueStatus.DONE.value

        waiting = QueueRepository.get_waiting_queue(
            shop.id,
            today,
        )

        if waiting:
            waiting.status = QueueStatus.SERVING.value

        QueueRepository.commit()

        current = QueueRepository.get_current_queue(
            shop.id,
            today,
        )

        last = QueueRepository.get_last_queue(
            shop.id,
            today,
        )

        current_number = current.queue_number if current else None
        last_number = last.queue_number if last else 0
        remaining = (
            last_number - current_number
            if current_number is not None
            else last_number
        )

        return {
            "current_queue": current_number,
            "last_queue": last_number,
            "remaining": remaining,
            "status": current.status if current else "EMPTY",
        }