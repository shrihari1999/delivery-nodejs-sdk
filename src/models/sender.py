from internal_types import TypedDict

class Sender(TypedDict, total=True):
    stopId: str
    name: str
    phone: str

