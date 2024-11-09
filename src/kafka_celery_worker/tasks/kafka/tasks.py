import logging

from kafka import KafkaConsumer
from kafka.errors import KafkaTimeoutError

from kafka_celery_worker.core.config import settings
from kafka_celery_worker.worker import celery


@celery.task(
    name="kafka.read_messages",
)
def read_messages():
    """
    Read messages from Kafka topic and close connection and finish task.
    """
    logging.info("Connecting to Kafka server: %s", settings.KAFKA_SERVER)
    consumer = KafkaConsumer(
        settings.KAFKA_TOPIC,
        bootstrap_servers=settings.KAFKA_SERVER,
        group_id=settings.KAFKA_CONSUMER_GROUP,
        consumer_timeout_ms=settings.KAFKA_CONSUMER_TIMEOUT,  # Stop after 5 seconds of inactivity
    )
    logging.info("Connected to Kafka server: %s", settings.KAFKA_SERVER)
    logging.info("Reading messages from Kafka topic")
    try:
        for message in consumer:
            print(message.value.decode("utf-8"))
    except KafkaTimeoutError:
        logging.info(
            "No messages received in the last 5 seconds, stopping consumer."
        )
    finally:
        consumer.close()
        logging.info("Finished reading messages from Kafka topic")
