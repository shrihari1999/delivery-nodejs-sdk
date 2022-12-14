from .base import Base
from lalamove.response.driver import IDriver
from lalamove.http.driver import DriverHTTPClient

class Driver(Base):
    
    def retrieve(self, market: str, id: str, orderId: str) -> IDriver:
        httpClient = DriverHTTPClient(self.config)
        response = httpClient.get(market, f"/v3/orders/${orderId}/drivers/${id}")
        return response

    def cancel(self, market: str, id: str, orderId: str, reason: str) -> bool:
        httpClient = DriverHTTPClient(self.config)
        httpClient.delete(market, f"/v3/orders/${orderId}/drivers/${id}", {'reason': reason })
        return True
