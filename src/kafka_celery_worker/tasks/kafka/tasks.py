from kafka import KafkaConsumer

from kafka_celery_worker.core.config import settings
from kafka_celery_worker.worker import celery


@celery.task(
    name="kafka.read_messages",
)
def read_messages():
    # Connect to Kafka
    consumer = KafkaConsumer(
        settings.KAFKA_TOPIC,
        bootstrap_servers=settings.KAFKA_SERVER,
        group_id="kafka-celery-worker",
    )
    # Read messages and print them
    for message in consumer:
        print(message.value.decode("utf-8"))
