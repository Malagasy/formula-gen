FROM python:3.7.2-alpine

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt