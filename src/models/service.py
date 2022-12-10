from internal_types import TypedDict, List
from dimensions import Dimensions
from measurement import Measurement
from specialRequest import SpecialRequest
from deliveryItemSpec import DeliveryItemSpec

class Service(TypedDict, total=True):
    key: str
    description: str
    dimensions: Dimensions
    load: Measurement
    specialRequests: List[SpecialRequest]
    deliveryItemSpec: DeliveryItemSpec


##### END OF LSP SPECS
