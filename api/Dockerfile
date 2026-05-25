FROM  python:3.8.13-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /api
 

COPY . .

RUN pip install django==4.0.0 django-cors-headers==3.13.0 psycopg2-binary==2.9.5

EXPOSE 8000