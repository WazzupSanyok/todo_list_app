FROM python:3.11

RUN mkdir /app
WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN pip3 install -r requirements.txt