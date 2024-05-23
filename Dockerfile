FROM python:3.7-alpine

RUN apk update && apk upgrade
RUN apk add g++ python3-dev
# See https://archlinuxarm.org/forum/viewtopic.php?p=64598#p64598
RUN CFLAGS="-fcommon" pip3 install RPi.GPIO
RUN pip3 install adafruit-circuitpython-dht
RUN apk del g++ python3-dev

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests/

WORKDIR /src

ENTRYPOINT ["/bin/ash"]