from lalamove.response.quotation import IQuotation
from .base import BaseHTTPClient
from lalamove.payload.quotationPayload import QuotationPayload

class QuotationHTTPClient(BaseHTTPClient):
    
    # @private
    @staticmethod
    def toIQuotation(quotation) -> IQuotation:
        quotation['id'] = quotation.pop('quotationId')
        if quotation.get('stops'):
            for stop in quotation['stops']:
                stop['id'] = stop.pop('stopId')

        return IQuotation(quotation)

    def create(self, market: str, path: str, body: QuotationPayload) -> IQuotation:
        try:
            response = self.makeCall(market, path, body, "POST")
        except Exception as e:
            QuotationHTTPClient.errorHandler(e)

        return QuotationHTTPClient.toIQuotation(response)

    def get(self, market: str, path: str) -> IQuotation:
        try:
            response = self.makeCall(market, path)
        except Exception as e:
            QuotationHTTPClient.errorHandler(e)

        return QuotationHTTPClient.toIQuotation(response)
