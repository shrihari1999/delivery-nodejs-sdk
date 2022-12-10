

class ICity(TypedDict, total=True):
    id: str
    name: str
    services: List[Service]
