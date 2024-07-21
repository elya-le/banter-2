FROM python:3.9.18-alpine3.18

RUN apk add build-base

RUN apk add postgresql-dev gcc python3-dev musl-dev

ARG FLASK_APP
ARG FLASK_ENV
ARG DATABASE_URL
ARG SCHEMA
ARG SECRET_KEY

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_BUCKET_NAME
ARG AWS_REGION

WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN flask db upgrade
RUN flask seed all

# this has been updated for: running with eventlet
CMD gunicorn -k eventlet -w 1 app:app 
