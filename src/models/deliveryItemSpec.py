from internal_types import TypedDict, Optional, List

class DeliveryItemSpec(TypedDict, total=False):
    quantity: Optional[str]
    categories: Optional[List[str]]
    handlingInstructions: Optional[List[str]]
    weight: Optional[List[str]]
