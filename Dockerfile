# syntax=docker/dockerfile:1
FROM python:3
# FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt /src/

# Addition requirements to get PILLOW working
RUN pip install --upgrade pip setuptools wheel
RUN apt-get install -u zlib1g-dev libjpeg-dev
RUN pip install wheel


RUN pip install -r requirements.txt
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
COPY ./src /src/