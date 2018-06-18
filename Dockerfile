FROM kennethreitz/pipenv
RUN apt-get install -y cron
COPY ./api /app
COPY ./input /app/ingest
RUN touch /var/log/cron.log
