FROM python:3.12-alpine


RUN apk add build-base
RUN apk add linux-headers


RUN apk add git

RUN git clone https://github.com/pimoroni/inky && cd inky && ./install.sh



#RUN pip install inky
#RUN pip install pillow
#RUN pip install requests
#RUN pip install raspi-gpio
#RUN pip install rpi.gpio
COPY script.py script.py
CMD python script.py