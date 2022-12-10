from internal_types import TypedDict, Optional

class PriceBreakdown(TypedDict, total=False):
    base: Optional[str]
    extraMileage: Optional[str]
    surcharge: Optional[str]
    coupon: Optional[str]
    specialRequests: Optional[str]
    priorityFee: Optional[str]
    priorityFeeVat: Optional[str]
    specialVehicle: Optional[str]
    minimumSurcharge: Optional[str]
    discountCap: Optional[str]
    insurance: Optional[str]
    multiStopSurcharge: Optional[str]
    surchargeDiscount: Optional[str]
    vat: Optional[str]
    customerSupportDiscretionary: Optional[str]
    totalBeforeOptimization: Optional[str]
    totalExcludePriorityFee: Optional[str]
    total: str
    currency: str
