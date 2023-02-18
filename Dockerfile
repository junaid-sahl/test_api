FROM python:3.9.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

#FROM python:3.9.10-alpine
#
#COPY . /test_api
#WORKDIR /test_api
#
#RUN apk add --no-cache mariadb-connector-c-dev
#RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base
#
#RUN apk add netcat-openbsd
#
#RUN pip install -r requirements.txt
