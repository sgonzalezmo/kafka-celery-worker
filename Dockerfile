# pull official base image
FROM python:3.12.2-alpine
# upgrade pip to the latest version
RUN apk --no-cache upgrade \
    && pip install --upgrade pip \
    && apk --no-cache add tzdata build-base gcc libc-dev g++ make git bash
RUN git clone https://github.com/edenhill/librdkafka.git && cd librdkafka \
    && git checkout tags/v2.6.0 && ./configure --clean \
    && ./configure --prefix /usr/local \
    && make && make install
# installing dependencies
COPY requirements/common.txt ./
RUN pip install -r common.txt --no-cache-dir
# copy application source code
COPY src .
# execute the application
CMD ["celery", "-A", "kafka_celery_worker.worker", "worker", "--loglevel=INFO"]
