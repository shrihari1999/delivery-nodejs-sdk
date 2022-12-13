from lalamove.response.city import ICity
from .base import Base
from lalamove.http.city import CityHTTPClient

marketsPath = "/v3/cities"

class City(Base):
    def retrieve(self, market: str, id: str) -> ICity:
        httpClient = CityHTTPClient(self.config)
        response = httpClient.get(market, id, marketsPath)
        return response

