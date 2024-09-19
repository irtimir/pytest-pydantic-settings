from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class SomeSettings(BaseSettings):
    key: str = Field(default='...', alias='KEY')

    model_config = SettingsConfigDict(extra="ignore",
                                      env_file_encoding="utf-8",
                                      env_file="tests/functional/.env",
                                      populate_by_name=True)
