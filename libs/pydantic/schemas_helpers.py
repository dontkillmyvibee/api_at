from typing import Any

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelCaseSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        from_attributes=True,
        populate_by_name=True,
        extra="forbid",
    )

    def model_dump_by_alias(self) -> dict[str, Any]:
        return self.model_dump(by_alias=True)
