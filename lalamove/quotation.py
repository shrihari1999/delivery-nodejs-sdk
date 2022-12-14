from .base import Base
from lalamove.response.quotation import IQuotation
from lalamove.payload.quotationPayload import QuotationPayload
from lalamove.http.quotation import QuotationHTTPClient

quotationPath = "/v3/quotations"

class Quotation(Base):
    def create(self, market: str, quotationPayload: QuotationPayload) -> IQuotation:
        httpClient = QuotationHTTPClient(self.config)
        response = httpClient.create(market, quotationPath, quotationPayload)
        return response

    def retrieve(self, market: str, orderId: str) -> IQuotation:
        httpClient = QuotationHTTPClient(self.config)
        response = httpClient.get(market, f'{quotationPath}/{orderId}')
        return response
