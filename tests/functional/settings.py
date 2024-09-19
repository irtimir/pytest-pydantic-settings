from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class SomeSettings(BaseSettings):
    key: str = Field(default='...', json_schema_extra={'key': 'SOME_KEY'})

    model_config = SettingsConfigDict(
        env_file='tests/functional/.env',
    )
