from enum import Enum


class QueueStatus(str, Enum):
    WAITING = "WAITING"
    CALLING = "CALLING"
    DONE = "DONE"