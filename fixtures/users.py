import pytest
from pydantic import BaseModel, UUID4, EmailStr
from clients.gateway.users.client import UsersHTTPClient, build_users_http_client
from clients.gateway.users.schemas import CreateUserRequestSchema, CreateUserResponseSchema


@pytest.fixture
def http_users_client() -> UsersHTTPClient:
    return build_users_http_client()

class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def user_id(self) -> UUID4:
        return self.response.user.id

    @property
    def response_email(self) -> EmailStr:
        return self.response.user.email

    @property
    def response_last_name(self) -> str:
        return self.response.user.last_name

    @property
    def response_first_name(self) -> str:
        return self.response.user.first_name

    @property
    def response_middle_name(self) -> str:
        return self.response.user.middle_name

    @property
    def response_phone_number(self) -> str:
        return self.response.user.phone_number

    @property
    def response_full_name(self) -> str:
        return f"{self.response.user.first_name} {self.response.user.last_name}"

@pytest.fixture
def function_user(http_users_client: UsersHTTPClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = http_users_client.create_user(request)

    return UserFixture(request=request, response=response)