FROM python:3.11

RUN apt update -y && apt upgrade -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#ENV STATICFILES_HOME=/tmp/staticfiles

#RUN mkdir -p $STATICFILES_HOME

WORKDIR /home/app/web

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .