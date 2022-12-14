from .base import Base
from lalamove.response.order import IOrder
from lalamove.payload.orderPayload import OrderPayload
from lalamove.http.order import OrderHTTPClient
from lalamove.payload.order.patchOrderPayload import PatchOrderPayload

orderPath = "/v3/orders"

class Order(Base):
    
    def create(self, market: str, orderPayload: OrderPayload) -> IOrder:
        httpClient = OrderHTTPClient(self.config)
        response = httpClient.post(market, orderPath, orderPayload)
        return response

    def edit(self, market: str, orderId: str, patchOrderPayload: PatchOrderPayload) -> IOrder:
        httpClient = OrderHTTPClient(self.config)
        response = httpClient.patch(market, f"{orderPath}/{orderId}", patchOrderPayload)
        return response

    def retrieve(self, market: str, orderId: str) -> IOrder:
        httpClient = OrderHTTPClient(self.config)
        response = httpClient.get(market, f"{orderPath}/{orderId}")
        return response

    def cancel(self, market: str, orderId: str) -> bool:
        httpClient = OrderHTTPClient(self.config)
        httpClient.delete(market, f"{orderPath}/{orderId}")
        return True

    def addPriorityFee(self, market: str, orderId: str, fee: str) -> bool:
        httpClient = OrderHTTPClient(self.config)
        httpClient.post_priorityfee(
            market, f"{orderPath}/{orderId}/priority-fee", {"priorityFee": fee}
        )
        return True
