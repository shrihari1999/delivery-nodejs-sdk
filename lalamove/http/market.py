from lalamove.models.internal_types import List
from .base import BaseHTTPClient
from lalamove.response.market import IMarket, ICity

class MarketHTTPClient(BaseHTTPClient):
    def get(self, market: str, path: str) -> IMarket:
        try:
            d = self.makeCall(market, path)
        except Exception as e:
            MarketHTTPClient.errorHandler(e)

        cities: List[ICity] = [
            ICity(id=city['locode'],
            **{k: city[k] for k in city.keys() if k != 'locode'})
            for city in d
        ]

        i_market = IMarket(
            id=market, 
            cities=cities
        )

        return i_market
