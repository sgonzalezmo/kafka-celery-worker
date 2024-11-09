from kafka_celery_worker.worker import celery


@celery.task
def task_every_10_seconds():
    print("Task executed every 10 seconds")
