import pytest
from http import HTTPStatus

from assertions.users.assertions import assert_create_user_response
from clients.gateway.users.client import UsersHTTPClient
from clients.gateway.users.schemas import CreateUserRequestSchema, CreateUserResponseSchema
from libs.assertions.base_assertions import assert_status_code
from libs.faker.faker import fake


class TestCreateUser:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "icloud.com", "outlook.com", "example.com"])
    def test_create_user(self, http_users_client: UsersHTTPClient, domain: str) -> None:
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        response = http_users_client.create_user_api(request=request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request=request, response=response_data)


class TestCreateUserNegative:
    @pytest.mark.parametrize(
        "email",
        [
            "without_domain@",
            "withoutspecsgmail.com",
            "outlook.com",
            "",
            "1",
            "@gmail.com",
        ],
    )
    def test_create_user_with_invalid_email(self, email: str, http_users_client: UsersHTTPClient) -> None:
        request = CreateUserRequestSchema.model_construct(email=email)
        response = http_users_client.create_user_api(request=request)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
