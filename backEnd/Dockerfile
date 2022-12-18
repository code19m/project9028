FROM python:3.10-slim-buster

WORKDIR /backEnd

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat libpq-dev gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /backEnd/requirements.txt
RUN pip install -r requirements.txt

COPY . /backEnd