from lalamove.models.internal_types import List, Optional
from lalamove.models.patchOrderStop import PatchOrderStop
from operator import itemgetter

class PatchOrderPayload:
    stops: Optional[List[PatchOrderStop]]

    def __init__(self, builder) -> None:
        stops = itemgetter('stops')(builder)
        stopsLength = len(stops or [])

        if stopsLength > 17 or stopsLength < 2:
            raise Exception("Stops must be between 2 and 17")

        if not all(map(lambda stop: stop.get('address'), stops or [])):
            raise Exception("Address cannot be empty")

        self.stops = stops

