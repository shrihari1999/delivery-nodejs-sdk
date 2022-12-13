from lalamove.http.base import BaseHTTPClient
from lalamove.response.city import ICity

class CityHTTPClient(BaseHTTPClient):
    def get(self, market: str, id: str, path: str) -> ICity:
        try:
            d = self.makeCall(market, path)
        except Exception as e:
            CityHTTPClient.errorHandler(e)
        
        for curr in d:
            curr['id'] = curr.pop('locode')

        IMarket = {
            'id': market,
            'cities': d,
        }
        for currCity in IMarket['cities']:
            if currCity['id'] == id:
                return ICity(currCity)
        
        raise Exception("No such city")