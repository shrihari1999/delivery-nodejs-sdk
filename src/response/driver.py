class IDriver(TypedDict, total=True):
    id: str
    contact: Contact
    plateNumber: str
    photo: str
    coordinates: Coordinates
    updatedAt: 'Date'
