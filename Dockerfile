FROM python:3.12.3-slim

RUN mkdir project
WORKDIR project

ADD . /project/
ADD .env.docker /project/.env

ENV APP_NAME=DOCKER_DEMO

WORKDIR requirements
RUN pip install -r dev.txt
WORKDIR ..

CMD gunicorn my_site.wsgi:application -b 0.0.0.0:8000