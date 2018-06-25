FROM kennethreitz/pipenv
COPY . /app
RUN apt-get install -y cron logrotate
COPY ./app/ingest/logrotate.conf /etc/logrotate.d/ingest
RUN touch /var/log/cron.log
