FROM python:3.12.3-slim

WORKDIR /master/
ENV PYTHONPATH /master/
ENV PYTHONUNBUFFERED 1


COPY requirements.txt /requirements.txt

RUN apt-get update -o Acquire::Check-Valid-Until=false && \
    apt-get -o Acquire::Max-FutureTime=86400 install -y build-essential libpq-dev ncat netcat-traditional


RUN pip install -r /requirements.txt


COPY . .