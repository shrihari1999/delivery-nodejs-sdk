from lalamove.models.internal_types import TypedDict, List
from lalamove.response.city import ICity

class IMarket(TypedDict, total=True):
    id: str
    cities: List[ICity]

