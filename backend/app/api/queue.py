from flask import Blueprint

from app.services.queue_service import QueueService
from app.utils.response import success

queue_bp = Blueprint(
    "queue",
    __name__,
    url_prefix="/api",
)


@queue_bp.post("/shops/<string:public_code>/queue")
def take_queue(public_code: str):

    result = QueueService.take_queue(public_code)

    return success(
        result,
        status_code=201,
    )


@queue_bp.get("/shops/<string:public_code>/queue")
def get_queue(public_code):

    result = QueueService.get_status(public_code)

    return success(result)


@queue_bp.post("/shops/<string:public_code>/queue/next")
def next_queue(public_code):

    result = QueueService.next_queue(public_code)

    return success(result)