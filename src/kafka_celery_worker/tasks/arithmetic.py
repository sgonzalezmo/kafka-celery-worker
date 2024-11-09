from kafka_celery_worker.worker import celery


@celery.task(
    name="arithmetic.add",
)
def add(x, y):
    return x + y


@celery.task(
    name="arithmetic.subtract",
)
def subtract(x, y):
    return x - y


@celery.task(
    name="arithmetic.multiply",
)
def multiply(x, y):
    return x * y


@celery.task(
    name="arithmetic.divide",
)
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
