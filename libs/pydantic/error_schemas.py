from libs.pydantic.schemas_helpers import CamelCaseSchema


class ValidationErrorSchema(CamelCaseSchema):
    loc: list[str | int]
    msg: str
    type: str


class HTTPInternalErrorSchema(CamelCaseSchema):
    detail: str


class HTTPValidationErrorSchema(CamelCaseSchema):
    detail: list[ValidationErrorSchema] | None = None
