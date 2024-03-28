FROM python:3.13.0a4-alpine3.19

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app/ .
RUN chmod 555 run.sh
RUN chmod 777 log/worker.log

EXPOSE 7000

CMD './run.sh'