FROM python:3.6-alpine
WORKDIR /
RUN apk update && \
    apk add git
RUN git clone https://github.com/achyut3598/hw2.git hw2
WORKDIR /hw2
CMD [ "python", "-u", "hw2.py" ]