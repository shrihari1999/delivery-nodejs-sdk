from enum import Enum
import re

class CallerModule(Enum):
    PostQuotation = 1
    GetQuotation = 2
    PostOrder = 3
    PatchOrder = 4
    GetOrder = 5
    CancellOrder = 6
    GetDriver = 7
    ChangeDriver = 8
    GetMarket = 9
    PostWebhook = 10
    AddPriorityFee = 11


def defineCallerModule(path: str, method: str) -> CallerModule:
    if method == "POST" and path == "/v3/quotations":
        return CallerModule.PostQuotation

    if method == "GET" and path.includes("/v3/quotations/"):
        return CallerModule.GetQuotation

    if method == "POST" and path == "/v3/orders":
        return CallerModule.PostOrder

    if method == "PATCH" and re.findall(r"/v3/order/(.*)$", path):
        return CallerModule.PatchOrder

    if method == "GET" and re.findall(r"/v3/order/(.*)$", path):
        return CallerModule.GetOrder

    if method == "DELETE" and re.findall(r"/v3/order/(.*)$", path):
        return CallerModule.CancellOrder

    if method == "GET" and re.findall(r"/v3/order/(.*)/driver/(.*)$", path):
        return CallerModule.GetDriver

    if method == "DELETE" and re.findall(r"/v3/order/(.*)/driver/(.*)$", path):
        return CallerModule.ChangeDriver

    if method == "GET" and path.includes("/v3/cities"):
        return CallerModule.GetMarket

    if method == "POST" and path == "/v3/webhook":
        return CallerModule.PostWebhook

    return CallerModule.AddPriorityFee
