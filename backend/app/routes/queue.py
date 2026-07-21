from flask import Blueprint

from flask import jsonify

from app.services.queue_service import QueueService

queue_bp = Blueprint(
    "queue",
    __name__,
    url_prefix="/api",
)

@queue_bp.post("/shops/<string:public_code>/queue")
def take_queue(public_code: str):

    result = QueueService.take_queue(public_code)

    if result is None:
        return (
            jsonify(
                {
                    "message": "Shop not found",
                }
            ),
            404,
        )

    return jsonify(result), 201
  
@queue_bp.get("/shops/<string:public_code>/queue")
def get_queue(public_code):

    result = QueueService.get_status(public_code)

    if result is None:
        return (
            jsonify(
                {
                    "message": "Shop not found",
                }
            ),
            404,
        )

    return jsonify(result)
  
@queue_bp.post("/shops/<string:public_code>/queue/next")
def next_queue(public_code):

    result = QueueService.next_queue(public_code)

    if result is None:
        return (
            jsonify(
                {
                    "message": "Shop not found",
                }
            ),
            404,
        )

    return jsonify(result)