import pytest
import allure

from libs.allure.enums import AllureTag, AllureEpic, AllureFeature, AllureSuite, AllureStory, AllureParent, \
    AllureSubSuite


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.api
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.USERS_SERVICE)
@allure.feature(AllureFeature.USER_MANAGEMENT)
@allure.parent_suite(AllureParent.API)
@allure.suite(AllureSuite.GET_USERS)
@allure.story(AllureStory.GET_USER)
class TestGetUserHelper:...

@pytest.mark.positive
@allure.sub_suite(AllureSubSuite.POSITIVE)
class TestGetUserPositiveHelper(TestGetUserHelper):...

@pytest.mark.negative
@allure.sub_suite(AllureSubSuite.NEGATIVE)
class TestGetUserNegativeHelper(TestGetUserHelper):...