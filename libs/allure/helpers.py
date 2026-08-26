import contextlib
import json
import allure

from requests import Response


def attach_response(response: Response) -> None:
    body = response.text
    with contextlib.suppress(ValueError):
        body = json.dumps(response.json(), ensure_ascii=False, indent=2)

    content = f"Status: {response.status_code} {response.reason}\n\n{body}"
    allure.attach(content, "Response body", allure.attachment_type.TEXT)
