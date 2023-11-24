from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env.bot', env_file_encoding='utf-8')

    TOKEN: str
    BACKEND_BASE_URL: str


CONFIG = Settings()
