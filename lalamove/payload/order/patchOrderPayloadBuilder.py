from lalamove.models.internal_types import List, Optional
from lalamove.models.patchOrderStop import PatchOrderStop
from .patchOrderPayload import PatchOrderPayload

class PatchOrderPayloadBuilder:
    stops: Optional[List[PatchOrderStop]]

    @staticmethod
    def patchOrderPayload() -> None:
        return PatchOrderPayloadBuilder()

    def withStops(self, stops: List[PatchOrderStop]) -> None:
        self.stops = stops
        return self

    def build(self) -> PatchOrderPayload:
        return PatchOrderPayload(self)

