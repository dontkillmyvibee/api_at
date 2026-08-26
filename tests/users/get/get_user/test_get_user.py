from http import HTTPStatus

from assertions.users.assertions import assert_get_user_response, assert_user_not_found
from clients.gateway.users.client import UsersHTTPClient
from clients.gateway.users.schemas import GetUserResponseSchema
from fixtures.users import UserFixture
from libs.assertions.base_assertions import assert_status_code
from libs.faker.faker import fake


class TestGetUser:
    def test_get_user_by_id(self, http_users_client: UsersHTTPClient, function_user: UserFixture) -> None:
        response = http_users_client.get_user_api(user_id=function_user.response.user.id)
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(user=function_user, response=response_data)


class TestGetUserNegative:
    def test_get_user_with_invalid_id(self, http_users_client: UsersHTTPClient) -> None:
        user_id = fake.uuid()
        response = http_users_client.get_user_api(user_id=user_id)

        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)
        assert_user_not_found(actual=response, user_id=user_id)
