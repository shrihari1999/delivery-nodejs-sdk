from .quotationPayload import QuotationPayload
from lalamove.models.internal_types import Union, List, Optional
from lalamove.models.stop import Stop
from lalamove.models.item import Item
from datetime import datetime

class QuotationPayloadBuilder:
    __scheduleAt: Optional[datetime]

    __serviceType: str

    __specialRequests: Optional[List[str]]

    __language: Union[str, None]

    __stops: List[Stop]

    __isRouteOptimized: Optional[bool]

    __item: Optional[Item]

    @staticmethod
    def quotationPayload() -> None:
        return QuotationPayloadBuilder()

    def withScheduleAt(self, scheduleAt: datetime) -> None:
        self.__scheduleAt = scheduleAt
        return self

    def withServiceType(self, serviceType: str) -> None:
        self.__serviceType = serviceType
        return self

    def withSpecialRequests(self, specialRequests: List[str]) -> None:
        self.__specialRequests = specialRequests
        return self

    def withLanguage(self, language: str) -> None:
        self.__language = language
        return self

    def withStops(self, stops: List[Stop]) -> None:
        self.__stops = stops
        return self

    def withIsRouteOptimized(self, isRouteOptimized: bool) -> None:
        self.__isRouteOptimized = isRouteOptimized
        return self

    def withItem(self, item: Item) -> None:
        self.__item = item
        return self

    def build(self) -> QuotationPayload:
        return QuotationPayload(self)
