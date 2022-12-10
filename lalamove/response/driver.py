from lalamove.models.internal_types import TypedDict
from lalamove.models.contact import Contact
from lalamove.models.coordinates import Coordinates
from datetime import datetime

class IDriver(TypedDict, total=True):
    id: str
    contact: Contact
    plateNumber: str
    photo: str
    coordinates: Coordinates
    updatedAt: datetime
