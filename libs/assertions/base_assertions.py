from typing import Any, Container

import allure
from libs.logger.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")


@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str) -> None:
    logger.info(f'Check that "{name}" equals to {expected}')

    assert actual == expected, f'Incorrect value: "{name}". Expected value: {expected}. Actual value: {actual}'


@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    assert_equal(actual, expected, "Status Code"), (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )


@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str) -> None:
    logger.info(f'Check that "{name}" is true')

    assert actual, f'Incorrect value: "{name}". Expected true value but got: {actual}'


@allure.step("Check that name in {expected}")
def assert_in(actual: Any, expected: Container[Any], name: str) -> None:
    logger.info(f'Check that "{name}" in {expected}')
    assert actual in expected, (
        f"Object {name} not found in {expected}."
        f"Expected: {actual} in {expected} == True."
        f"Actual: {actual} in {expected} == False"
    )


@allure.step("Check that {name} isn`t None")
def assert_not_none(actual: Any, name: str) -> None:
    logger.info(f'Check that "{name}" isn`t None')
    assert actual is not None, f"Object {name} is None.Expected: {actual} != None.Actual: {actual} == None"
