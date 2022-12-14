from lalamove.models.internal_types import Any
from lalamove.response.order import IOrder
from lalamove.http.base import BaseHTTPClient
from lalamove.payload.orderPayload import OrderPayload
from lalamove.payload.order.patchOrderPayload import PatchOrderPayload

class OrderHTTPClient(BaseHTTPClient):
    
    # @private
    @staticmethod
    def toIOrder(order: Any) -> IOrder:
        order['id'] = order.pop('orderId')
        for stop in order['stops']:
            if stop.get('stopId'):
                stop['id'] = stop.pop('stopId')
        
        return IOrder(order)

    def post(self, market: str, path: str, body: OrderPayload) -> IOrder:
        try:
            response = self.makeCall(market, path, body, "POST")
        except Exception as e:
            OrderHTTPClient.errorHandler(e)
        
        return OrderHTTPClient.toIOrder(response)


    def get(self, market: str, path: str) -> IOrder:
        try:
            response = self.makeCall(market, path)
        except Exception as e:
            OrderHTTPClient.errorHandler(e)
        
        return OrderHTTPClient.toIOrder(response)


    def delete(self, market: str, path: str) -> bool:
        try:
            response = self.makeCall(market, path, None, "DELETE")
        except Exception as e:
            OrderHTTPClient.errorHandler(e)
        
        return True

    def post_priorityfee(self, market: str, path: str, priorityFee: dict) -> bool:
        try:
            response = self.makeCall(market, path, priorityFee, "POST")
        except Exception as e:
            OrderHTTPClient.errorHandler(e)
        
        return True

    def patch(self, market: str, path: str, body: PatchOrderPayload) -> IOrder:
        try:
            response = self.makeCall(market, path, body, "PATCH")
        except Exception as e:
            OrderHTTPClient.errorHandler(e)
        
        return OrderHTTPClient.toIOrder(response)

