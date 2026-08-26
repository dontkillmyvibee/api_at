from http import HTTPStatus

from assertions.users.assertions import assert_get_user_response
from clients.gateway.users.client import UsersHTTPClient
from clients.gateway.users.schemas import GetUserResponseSchema
from fixtures.users import UserFixture
from libs.assertions.base_assertions import assert_status_code


class TestGetUser:
    def test_get_user_by_id(self, http_users_client: UsersHTTPClient, function_user: UserFixture) -> None:
        response = http_users_client.get_user_api(user_id=function_user.response.user.id)
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(user=function_user, response=response_data)
