FROM python:3.9-slim-buster AS base

RUN apt update && apt install -y iputils-ping && pip3 install flask

FROM base AS builder

WORKDIR /app

COPY  app/* ./

EXPOSE 8080

USER www-data

CMD ["python", "app.py"]