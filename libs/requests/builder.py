from requests import Session

from libs.requests.base_client import HTTPClient


def build_http_client(base_url: str, timeout: int, headers: dict[str, str] | None = None) -> HTTPClient:
    session = Session()

    if headers:
        session.headers.update(headers)

    return HTTPClient(session=session, base_url=base_url, timeout=timeout)
