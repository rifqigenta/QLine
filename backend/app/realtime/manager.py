from queue import Queue


class EventManager:

    def __init__(self):
        self.clients = []

    def subscribe(self):

        q = Queue()

        self.clients.append(q)

        return q

    def unsubscribe(self, q):

        if q in self.clients:
            self.clients.remove(q)

    def publish(self, data):

        for client in self.clients:
            client.put(data)


event_manager = EventManager()