FROM kennethreitz/pipenv

COPY ./app /app
RUN apt-get install -y cron logrotate
COPY ./input /app/ingest
COPY ./input/logrotate.conf /etc/logrotate.d/ingest
RUN touch /var/log/cron.log
