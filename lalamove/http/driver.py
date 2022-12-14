from lalamove.response.driver import IDriver
from .base import BaseHTTPClient
from lalamove.models.contact import Contact
from datetime import datetime

class DriverHTTPClient(BaseHTTPClient):

    @staticmethod
    def toIDriver(driver):
        driver["id"] = driver.pop("driverId")
        contact:Contact = Contact({
            "name": driver.pop("name"),
            "phone": driver.pop("phone"),
        })
        driver["updatedAt"] = driver["coordinates"].pop("updatedAt")
        if driver["updatedAt"]:
            driver["updatedAt"] = datetime.fromisoformat(driver["updatedAt"])
        driver["contact"] = contact
        return IDriver(driver)

    def get(self, market: str, path: str) -> IDriver:
        try:
            response = self.makeCall(market, path)
        except Exception as e:
            DriverHTTPClient.errorHandler(e)
        
        return DriverHTTPClient.toIDriver(response)

    def delete(self, market: str, path: str, reason: dict) -> bool:
        try:
            response = self.makeCall(market, path, reason, "DELETE")
        except Exception as e:
            DriverHTTPClient.errorHandler(e)
        
        return True

