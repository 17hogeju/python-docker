FROM python:3.6-alpine
WORKDIR /
RUN apk update && \
    apk add git
RUN git clone https://github.com/17hogeju/python-docker.git julia-hoge-hw
WORKDIR /julia-hoge-hw
CMD [ "python", "-u", "script.py" ]