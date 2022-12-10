from .internal_types import TypedDict

class Recipient(TypedDict, total=True):
    stopId: str
    name: str
    phone: str
    remarks: str
