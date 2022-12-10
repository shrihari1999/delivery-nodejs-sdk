from .internal_types import TypedDict

class Contact(TypedDict, total=True):
    name: str
    phone: str
