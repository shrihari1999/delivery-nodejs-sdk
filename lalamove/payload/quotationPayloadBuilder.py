from .quotationPayload import QuotationPayload
from lalamove.models.internal_types import Union, List, Optional
from lalamove.models.stop import Stop
from lalamove.models.item import Item
from datetime import datetime

class QuotationPayloadBuilder:
    scheduleAt: Optional[datetime]

    serviceType: str

    specialRequests: Optional[List[str]]

    language: Union[str, None]

    stops: List[Stop]

    isRouteOptimized: Optional[bool]

    item: Optional[Item]

    @staticmethod
    def quotationPayload() -> None:
        return QuotationPayloadBuilder()

    def withScheduleAt(self, scheduleAt: datetime) -> None:
        self.scheduleAt = scheduleAt
        return self

    def withServiceType(self, serviceType: str) -> None:
        self.serviceType = serviceType
        return self

    def withSpecialRequests(self, specialRequests: List[str]) -> None:
        self.specialRequests = specialRequests
        return self

    def withLanguage(self, language: str) -> None:
        self.language = language
        return self

    def withStops(self, stops: List[Stop]) -> None:
        self.stops = stops
        return self

    def withIsRouteOptimized(self, isRouteOptimized: bool) -> None:
        self.isRouteOptimized = isRouteOptimized
        return self

    def withItem(self, item: Item) -> None:
        self.item = item
        return self

    def build(self) -> QuotationPayload:
        return QuotationPayload(self)
