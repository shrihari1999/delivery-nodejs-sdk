class IQuotation(TypedDict, total=True):
    id: str
    scheduleAt: 'Date'
    serviceType: str
    specialRequests: List[str]
    expiresAt: 'Date'
    priceBreakdown: PriceBreakdown
    isRouteOptimized: bool
    stops: List[Stop]

