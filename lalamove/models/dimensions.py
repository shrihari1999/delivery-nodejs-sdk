from .internal_types import TypedDict
from .measurement import Measurement

class Dimensions(TypedDict, total=True):
    width: Measurement
    height: Measurement
    depth: Measurement
