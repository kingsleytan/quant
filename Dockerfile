FROM python:3.7.3-alpine

RUN apk add --update alpine-sdk

ARG WORKING_DIR=/app
COPY ./ $WORKING_DIR
WORKDIR $WORKING_DIR

RUN pip3 install --no-cache-dir -r $WORKING_DIR/requirements.txt

EXPOSE 8083

CMD python3 src/Server.py