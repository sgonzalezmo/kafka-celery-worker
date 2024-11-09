from kafka_celery_worker.worker import celery


@celery.task(
    name="kafka.read_messages",
)
def read_messages():
    print("Reading messages from Kafka")
