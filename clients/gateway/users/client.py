import allure
from pydantic import UUID4
from requests import Response

from clients.gateway.users.schemas import CreateUserRequestSchema, GetUserResponseSchema, CreateUserResponseSchema
from libs.http.enums import HTTPRoutes
from libs.requests.base_client import HTTPClient
from libs.requests.public_builder import get_public_http_client


class UsersHTTPClient:
    def __init__(self, client: HTTPClient):
        self.__client = client

    @allure.step('Get user by id "{user_id}"')
    def get_user_api(self, user_id: UUID4) -> Response:
        return self.__client.get(url=f'{HTTPRoutes.USERS}/{user_id}')

    @allure.step('Create user')
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        return self.__client.post(url=HTTPRoutes.USERS, json=request.model_dump_by_alias())

    def get_user(self, user_id: UUID4) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def build_users_http_client() -> UsersHTTPClient:
    return UsersHTTPClient(client=get_public_http_client())
