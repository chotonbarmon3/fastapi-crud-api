from pydantic_settings import BaseSettings,SettingsConfigDict

class settings(BaseSettings):
    url:str
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")

setting=settings()