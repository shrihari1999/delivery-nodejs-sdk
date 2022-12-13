from .base import Base
from lalamove.response.market import IMarket
from lalamove.http.market import MarketHTTPClient

marketsPath = "/v3/cities"

class Market(Base):
    def retrieve(self, market: str) -> IMarket:
        httpClient = MarketHTTPClient(self.config)
        response = httpClient.get(market, marketsPath)
        return response

