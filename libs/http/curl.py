import contextlib

from requests import PreparedRequest

ignore_headers = [
    "user-agent",
    "accept-encoding",
    "connection",
    "content-length",
]


def _single_quote(value: str) -> str:
    escaped = value.replace("'", "'\\''")
    return f"'{escaped}'"


def make_curl_from_prepared(prepared: PreparedRequest) -> str:
    result: list[str] = [
        f"curl -X {_single_quote(prepared.method or '')}",
        _single_quote(prepared.url or ""),
    ]

    for header, value in prepared.headers.items():
        if header.lower() not in ignore_headers:
            result.append(f"-H {_single_quote(f'{header}: {value}')}")

    if body := prepared.body:
        with contextlib.suppress(UnicodeDecodeError):
            decoded = body.decode("utf-8") if isinstance(body, bytes) else body
            result.append(f"-d {_single_quote(decoded)}")

    return " \\\n     ".join(result)
