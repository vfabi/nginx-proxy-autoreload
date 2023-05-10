FROM python:3.8-alpine

ADD app/redis-proxy /app
RUN pip3 install --upgrade pip && pip3 install -r  /app/requirements.txt
WORKDIR /app
# ENV PYTHONPATH "/app/"

ENTRYPOINT ["python3"]