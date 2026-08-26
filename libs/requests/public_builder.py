from config import get_settings
from libs.requests.base_client import HTTPClient
from libs.requests.builder import build_http_client


def get_public_http_client() -> HTTPClient:
    settings = get_settings()
    return build_http_client(base_url=settings.api.base_url_str, timeout=settings.api.timeout)
