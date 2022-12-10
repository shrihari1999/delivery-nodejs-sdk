from src.models.internal_types import TypedDict, List
from src.models.service import Service


class ICity(TypedDict, total=True):
    id: str
    name: str
    services: List[Service]
