FROM python:3.12-alpine


RUN apk add build-base
RUN apk add linux-headers

RUN pip install inky
RUN pip install pillow
RUN pip install requests
COPY script.py script.py
CMD python script.py