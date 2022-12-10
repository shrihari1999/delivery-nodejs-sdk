from internal_types import TypedDict

class SpecialRequest(TypedDict, total=True):
    name: str
    description: str
