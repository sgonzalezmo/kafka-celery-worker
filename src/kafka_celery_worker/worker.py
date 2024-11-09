from celery import Celery

from kafka_celery_worker.core import celeryconfig
from kafka_celery_worker.core.config import settings

celery = Celery(settings.APP_NAME)
# Set worker celery configuration
celery.config_from_object(celeryconfig)
# Register worker tasks
celery.autodiscover_tasks(
    [
        "kafka_celery_worker.tasks.kafka",
        "kafka_celery_worker.tasks.arithmetic",
    ]
)
