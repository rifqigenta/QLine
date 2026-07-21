from flask import Blueprint, Response
import json

from app.realtime.manager import event_manager

events_bp = Blueprint(
    "events",
    __name__,
)


@events_bp.get("/shops/<string:public_code>/events")
def events(public_code):
    print(">>> EVENTS ENDPOINT HIT:", public_code)

    def stream():
        
        print(">>> CLIENT SUBSCRIBED")

        q = event_manager.subscribe(public_code)

        try:

            while True:

                data = q.get()
                
                print(">>> SEND EVENT:", data)

                yield (
                    f"data: {json.dumps(data)}\n\n"
                )

        finally:
            
            print(">>> CLIENT DISCONNECTED")

            event_manager.unsubscribe(
                public_code,
                q,
            )

    return Response(
        stream(),
        mimetype="text/event-stream",
    )