FROM kennethreitz/pipenv
COPY ./app /app
RUN apt-get install -y cron rsyslog logrotate
COPY ./app/ingest/logrotate.conf /etc/logrotate.d/ingest
RUN mkdir /app/logs /app/ingest/config /app/ingest/data /app/ingest/debug 
RUN touch /var/log/cron.log
RUN ln -s /var/log/cron.log /app/logs/cron.log
RUN chmod +x /app/ingest/run.sh
