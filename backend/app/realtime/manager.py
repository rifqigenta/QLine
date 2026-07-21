from collections import defaultdict
from queue import Queue
from threading import Lock


class EventManager:

    def __init__(self):
        self.clients = defaultdict(list)
        self.lock = Lock()

    def subscribe(
        self,
        public_code: str,
    ):

        q = Queue()

        with self.lock:
            self.clients[public_code].append(q)

        return q

    def unsubscribe(
        self,
        public_code: str,
        q,
    ):

        with self.lock:

            if q in self.clients[public_code]:
                self.clients[public_code].remove(q)

            if not self.clients[public_code]:
                del self.clients[public_code]

    def publish(
        self,
        public_code: str,
        data: dict,
    ):

        with self.lock:

            clients = list(
                self.clients.get(public_code, [])
            )

        for client in clients:
            client.put(data)


event_manager = EventManager()