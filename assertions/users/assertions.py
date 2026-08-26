import allure
from requests import Response
from pydantic import UUID4

from clients.gateway.users.schemas import GetUserResponseSchema
from fixtures.users import UserFixture
from libs.assertions.base_assertions import assert_equal, assert_in
from libs.logger.logger import get_logger
from libs.pydantic.error_schemas import HTTPInternalErrorSchema

logger = get_logger("USER_ASSERTIONS")


@allure.step("Check get user response")
def assert_get_user_response(user: UserFixture, response: GetUserResponseSchema) -> None:
    logger.info("Check get user response")

    assert_equal(response.user.id, user.user_id, "user_id")
    assert_equal(response.user.email, user.response_email, "email")
    assert_equal(response.user.last_name, user.response_last_name, "last_name")
    assert_equal(response.user.first_name, user.response_first_name, "first_name")
    assert_equal(response.user.middle_name, user.response_middle_name, "middle_name")
    assert_equal(response.user.phone_number, user.response_phone_number, "phone_number")


@allure.step("Check user not found response")
def assert_user_not_found(actual: Response, user_id: UUID4) -> None:
    logger.info("Check user not found response")

    expected = f"User with id {user_id} not found"
    prep_actual = HTTPInternalErrorSchema.model_validate_json(actual.text)

    assert_in(expected, prep_actual.detail, "detail")
