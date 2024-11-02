FROM python:3.10.15-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8001

COPY . /app