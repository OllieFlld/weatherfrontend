FROM python:3.14.0-alpine


RUN apk add build-base
RUN apk add linux-headers

RUN pip install inky
RUN pip install pillow
RUN pip install requests

