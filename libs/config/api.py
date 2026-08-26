from pydantic import BaseModel, HttpUrl, Field


class HTTPClientSettings(BaseModel):
    base_url: HttpUrl
    timeout: int = Field(default=30, gt=0)

    @property
    def base_url_str(self) -> str:
        return str(self.base_url).rstrip("/")
