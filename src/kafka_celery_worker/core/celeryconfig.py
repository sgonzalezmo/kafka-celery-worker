from kafka_celery_worker.core.config import settings

broker_url = settings.CELERY_BROKER_URL
result_backend = settings.CELERY_RESULT_BACKEND
timezone = settings.TIMEZONE
