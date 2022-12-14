from lalamove.models.internal_types import Union, List, Optional
from lalamove.http.util import CallerModule
from datetime import datetime
import json

class IError:
    id: Optional[str]
    message: Optional[str]
    detail: Optional[str]

    def __init__(self, id: str = None, message: str = None, detail: str = None) -> None:
        self.id = id
        self.message = message
        self.detail = detail


class APIError(Exception):
    httpStatus: int

    errors: Optional[Union[IError, List[IError]]]

    date: datetime

    callerModule: CallerModule

    def __init__(self, cm: CallerModule, httpStatus: int, response: str, *args: object) -> None:
        # Pass remaining arguments (including vendor specific ones) to parent constructor
        super().__init__(*args)

        # Maintains proper stack trace for where our error was thrown (only available on V8)
        # if Error.captureStackTrace:
        #     Error.captureStackTrace(this, APIError)

        self.name = "APIError"
        # Custom debugging information
        self.httpStatus = httpStatus
        self.callerModule = cm

        try:
            r = json.loads(response)

            if type(r['errors']) is list:
                self.errors: List[IError] = [IError(e) for e in r['errors']]
            elif r['errors'] is not None and type(r['errors']) is dict:
                self.errors: IError = IError(r['errors'])
        except:
            unknown: IError = IError(
                message="Unknown error"
            )
            self.errors = unknown

        self.date = datetime.now()

    @staticmethod
    def mapErrorMessage(err: Union['APIError', Exception]) -> str:
        if not isinstance(err, APIError):
            return err.message

        schemaValidationErrors = ["ERR_INVALID_FIELD", "ERR_MISSING_FIELD"]
        e = err.getError()
        if err.errors and e.id and (e.id in schemaValidationErrors):
            what = e.detail.replace("/data/", "")
            why = e.message
            return f"Problem with {what} because of {why}"

        if err.httpStatus == 401:
            return "Please verify if you have made the request with the right credentials."

        if err.httpStatus == 429:
            return "You need to calm down. You hit the rate limit."

        if err.callerModule == CallerModule.PostOrder:
            if err.httpStatus == 402:
                return "Please check your wallet balance."

        if (
            err.callerModule == CallerModule.ChangeDriver or
            err.callerModule == CallerModule.GetDriver
        ):
            if err.httpStatus == 404:
                return "Driver not found."


        if err.callerModule == CallerModule.GetOrder:
            if err.httpStatus == 404:
                return "Order not found."


        if err.callerModule == CallerModule.GetQuotation:
            if err.httpStatus == 422 and e.id == "ERR_INVALID_QUOTATION_ID":
                return "Quotation not found."


        if e.message:
            return e.message

        if e.id:
            return e.id

        return "Unknown error"

    def getError(self) -> IError:
        if self.errors is None:
            return IError() #{}

        if type(self.errors) is list:
            e: List[IError] = self.errors
            return next(iter(e), None)

        return self.errors
