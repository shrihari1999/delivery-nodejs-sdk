from lalamove.models.internal_types import TypedDict, List, Dict
from lalamove.models.priceBreakdown import PriceBreakdown
from lalamove.models.measurement import Measurement
from lalamove.models.stop import StopWithContact
from lalamove.models.priceBreakdown import PriceBreakdown

class IOrder(TypedDict, total=True):
    id: str
    quotationId: str
    priceBreakdown: PriceBreakdown
    driverId: str
    shareLink: str
    status: str
    distance: Measurement
    stops: List[StopWithContact]
    metadata: Dict

