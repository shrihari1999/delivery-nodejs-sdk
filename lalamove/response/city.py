from lalamove.models.internal_types import TypedDict, List
from lalamove.models.service import Service


class ICity(TypedDict, total=True):
    id: str
    name: str
    services: List[Service]
