from pathlib import Path
from typing import Type, Tuple

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict, JsonConfigSettingsSource, PydanticBaseSettingsSource


CONFIG_FOLDER = Path(__file__).parent.parent / "secrets"


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    host: str
    port: int
    dbname: str
    user: str
    password: str
    pool_size: int = 5
    max_overflow: int = 10

    # naming_convention for base model class
    # it helps automatically generate alembic revisions with constraints or indexes
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        json_file_encoding="utf-8",
        json_file=(
            CONFIG_FOLDER / "settings.json",
            # "./secrets/settings.local.json",
        ),
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (JsonConfigSettingsSource(settings_cls),)


settings = Settings()
