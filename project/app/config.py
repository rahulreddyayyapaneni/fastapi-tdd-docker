import logging
import os
from functools import lru_cache
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT","dev")
    testing: bool = os.getenv("TESTING",0)

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading Config Settings From the Environment..")
    return Settings()
