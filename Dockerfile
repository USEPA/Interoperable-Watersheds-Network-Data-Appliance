FROM kennethreitz/pipenv

COPY ./app /app
RUN apt-get install -y cron
COPY ./input /app/ingest
RUN touch /var/log/cron.log
