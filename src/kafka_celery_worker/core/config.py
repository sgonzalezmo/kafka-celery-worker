from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application name
    APP_NAME: str = "kafka-celery-worker"
    # Variable for timezone
    TIMEZONE: str = "Europe/Madrid"
    # Celery environment variables
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    # Kafka environment variables
    KAFKA_SERVER: str
    KAFKA_TOPIC: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
