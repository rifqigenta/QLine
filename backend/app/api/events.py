from flask import Blueprint, Response
import json

from app.realtime.manager import event_manager

events_bp = Blueprint(
    "events",
    __name__,
)


@events_bp.get("/shops/<string:public_code>/events")
def events(public_code):

    def stream():

        q = event_manager.subscribe()

        try:

            while True:

                data = q.get()

                yield (
                    f"data: {json.dumps(data)}\n\n"
                )

        finally:

            event_manager.unsubscribe(q)

    return Response(
        stream(),
        mimetype="text/event-stream",
    )