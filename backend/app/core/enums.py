from enum import Enum


class QueueStatus(str, Enum):
    WAITING = "WAITING"
    SERVING = "SERVING"
    DONE = "DONE"
    CANCELLED = "CANCELLED"