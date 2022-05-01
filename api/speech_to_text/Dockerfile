FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /flask_app/requirements.txt

WORKDIR /speech_to_text
COPY . /speech_to_text

RUN pip3 install -r requirements.txt

ENTRYPOINT celery -A task worker --loglevel=info











