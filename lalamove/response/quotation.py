from lalamove.models.internal_types import TypedDict, List
from lalamove.models.priceBreakdown import PriceBreakdown
from lalamove.models.stop import Stop
from datetime import datetime

class IQuotation(TypedDict, total=True):
    id: str
    scheduleAt: datetime
    serviceType: str
    specialRequests: List[str]
    expiresAt: datetime
    priceBreakdown: PriceBreakdown
    isRouteOptimized: bool
    stops: List[Stop]

