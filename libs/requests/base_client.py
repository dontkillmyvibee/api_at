import allure
from http import HTTPMethod
from typing import Any

from requests import Response, Session, Request

from libs.allure.helpers import attach_response
from libs.http.curl import make_curl_from_prepared
from libs.logger.logger import get_logger

logger = get_logger("HTTP_CLIENT")


class HTTPClient:
    def __init__(self, session: Session, base_url: str, timeout: int) -> None:
        self.__session = session
        self.__base_url = base_url
        self.__timeout = timeout

    def __request(self, method: HTTPMethod, url: str, **kwargs: Any) -> Response:
        full_url = f"{self.__base_url}{url}"

        request = Request(method=method, url=full_url, **kwargs)
        prepared_request = self.__session.prepare_request(request)

        logger.info(f'Send request {prepared_request.method} to {prepared_request.url}')

        curl = make_curl_from_prepared(prepared_request)
        allure.attach(curl, "cURL", allure.attachment_type.TEXT)

        response = self.__session.send(prepared_request, timeout=self.__timeout)

        logger.info(f'Get response "{response.status_code} {response.reason}" from {response.url}')
        attach_response(response)
        return response

    def get(self, url: str, params: Any | None = None) -> Response:
        return self.__request(method=HTTPMethod.GET, url=url, params=params)

    def post(
            self,
            url: str,
            json: Any | None = None,
            data: Any | None = None,
            files: dict[str, Any] | None = None
    ) -> Response:
        return self.__request(method=HTTPMethod.POST, url=url, json=json, data=data, files=files)

    def patch(self, url: str, json: Any | None = None) -> Response:
        return self.__request(method=HTTPMethod.PATCH, url=url, json=json)

    def delete(self, url: str) -> Response:
        return self.__request(method=HTTPMethod.DELETE, url=url)
