from lalamove.models.internal_types import Union, List, Optional
from lalamove.models.stop import Stop
from lalamove.models.item import Item
from datetime import datetime

class QuotationPayload:
    __scheduleAt: Optional[datetime]

    __serviceType: str

    __specialRequests: Optional[List[str]]

    __language: Union[str, None]

    __stops: List[Stop]

    __isRouteOptimized: Optional[bool]

    __item: Optional[Item]

    def __init__(self, qpb) -> None:
        if qpb.serviceType == None:
            raise Exception("Service Type cannot be empty")

        if qpb.stops == None:
            raise Exception("Stops cannot be empty")

        self.__scheduleAt = qpb.scheduleAt
        self.__serviceType = qpb.serviceType
        self.__language = qpb.language
        self.__specialRequests = qpb.specialRequests
        self.__stops = qpb.stops
        self.__isRouteOptimized = qpb.isRouteOptimized
        self.__item = qpb.item

