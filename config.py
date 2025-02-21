from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    UVICORN_HOST: str
    UVICORN_PORT: int

    WEB_URL: str

    @property
    def uvicorn_host(self):
        return self.UVICORN_HOST

    @property
    def uvicorn_port(self):
        return self.UVICORN_PORT

    @property
    def web_url(self):
        return self.WEB_URL

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
