from .internal_types import TypedDict

class Measurement(TypedDict, total=True):
    value: str
    unit: str
