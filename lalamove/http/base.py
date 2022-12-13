import requests, sys, json
from lalamove.config import Config
from lalamove.auth import signRequest
from lalamove.error import APIError
from lalamove.models.internal_types import Union, Optional
from .util import defineCallerModule
from lalamove.version import __VERSION__
from datetime import datetime

class BaseHTTPClient:
    __config: Config

    def __init__(self, config: Config) -> None:
        self.__config = config


    @staticmethod
    def errorHandler(error: Union[Exception, APIError]):
        if isinstance(error, APIError):
            raise Exception(APIError.mapErrorMessage(error))
        else:
            raise error

    # @protected
    def makeCall(self, market: str, path: str, body: Optional[None] = None, method: str = "GET") -> requests.Response:
        pythonVersion = json.dumps(sys.version_info)
        timestamp = round(datetime.now().timestamp() * 1000)
        signature = signRequest(
            self.__config,
            method,
            path,
            timestamp,
            f'{"data": {json.dumps(body)}}' if body else None
        )
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json charset=UTF-8",
            "SDK-Type": "python",
            "SDK-Version": __VERSION__,
            "SDK-Language-Version": pythonVersion,
            "Authorization": f"hmac {self.__config.publicKey}:{timestamp}:{signature}",
            "Market": market,
        }
        if body:
            body = json.dumps({"data": json.dumps(body)})

        try:
            response = requests.request(
                method,
                'https://'+self.__config.host+path,
                headers=headers,
                json=body
            )
            if response.status_code > 299:
                raise APIError(
                    defineCallerModule(path, method),
                    response.status_code,
                    response.text,
                    'Something went wrong with your request'
                )
            elif len(response.text) == 0:
                return json.loads("{}")
            else:
                return response.json()['data']
        except Exception as e:
            print(f"Encountered an error trying to make a request: {e}")
            raise APIError(defineCallerModule(path, method), 0, "", e)

