from lalamove.models.internal_types import Union, List, Optional
from lalamove.models.stop import Stop
from lalamove.models.item import Item
from datetime import datetime

class QuotationPayload:
    scheduleAt: Optional[datetime]

    serviceType: str

    specialRequests: Optional[List[str]]

    language: Union[str, None]

    stops: List[Stop]

    isRouteOptimized: Optional[bool]

    item: Optional[Item]

    def __init__(self, qpb) -> None:
        if qpb.serviceType == None:
            raise Exception("Service Type cannot be empty")

        if qpb.stops == None:
            raise Exception("Stops cannot be empty")

        if getattr(qpb, 'scheduleAt', None) is not None:
            self.scheduleAt = qpb.scheduleAt
        
        self.serviceType = qpb.serviceType
        
        self.language = qpb.language
        
        if getattr(qpb, 'specialRequests', None) is not None:
            self.specialRequests = qpb.specialRequests
        
        self.stops = qpb.stops
        
        if getattr(qpb, 'isRouteOptimized', None) is not None:
            self.isRouteOptimized = qpb.isRouteOptimized
        
        if getattr(qpb, 'item', None) is not None:
            self.item = qpb.item
