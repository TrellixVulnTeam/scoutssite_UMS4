# syntax=docker/dockerfile:1
FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Create directory for the app user
RUN mkdir -p /home/app

#Create appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./