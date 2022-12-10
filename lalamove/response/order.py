
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

