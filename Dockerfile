FROM python:3.7.2-alpine as base

WORKDIR /www/app

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt