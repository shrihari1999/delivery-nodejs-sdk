from internal_types import TypedDict, Optional, List

class Item(TypedDict, total=False):
    quantity: Optional[str]
    weight: Optional[str]
    categories: Optional[List[str]]
    handlingInstructions: Optional[List[str]]
