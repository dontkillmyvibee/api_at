import pytest
import allure

from libs.allure.enums import AllureTag, AllureEpic, AllureFeature, AllureParent, AllureSuite, AllureSubSuite, \
    AllureStory


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.api
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.USERS_SERVICE)
@allure.feature(AllureFeature.USER_MANAGEMENT)
@allure.parent_suite(AllureParent.API)
@allure.suite(AllureSuite.POST_USERS)
@allure.story(AllureStory.CREATE_USER)
class TestCreateUserHelper: ...


@pytest.mark.positive
@allure.sub_suite(AllureSubSuite.POSITIVE)
class TestCreateUserPositiveHelper(TestCreateUserHelper):...

@pytest.mark.negative
@allure.sub_suite(AllureSubSuite.NEGATIVE)
class TestCreateUserNegativeHelper(TestCreateUserHelper):...