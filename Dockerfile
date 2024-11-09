# pull official base image
FROM python:3.12.2-alpine
# set work directory
WORKDIR /usr/src
# installing dependencies
COPY requirements/common.txt ./
RUN pip install -r common.txt --no-cache-dir
# copy application source code
COPY src .
# execute the application
CMD ["celery", "-A", "kafka_celery_worker.worker", "worker", "--loglevel=INFO"]
