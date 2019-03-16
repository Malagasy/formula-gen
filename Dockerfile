FROM python:3.7.2-alpine

WORKDIR /www/app

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

CMD python app.py