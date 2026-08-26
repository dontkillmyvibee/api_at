from enum import StrEnum


class AllureTag(StrEnum):
    USERS = 'USERS'
    REGRESSION = 'REGRESSION'


class AllureEpic(StrEnum):
    USERS_SERVICE = 'Users service API'

class AllureFeature(StrEnum):
    USER_MANAGEMENT = 'User Management'

class AllureParent(StrEnum):
    API = 'API'

class AllureSuite(StrEnum):
    POST_USERS = 'POST /users'
    GET_USERS = 'GET /users{user_id}'

class AllureStory(StrEnum):
    CREATE_USER = 'Create User'
    GET_USER = 'Get User'

class AllureSubSuite(StrEnum):
    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'
