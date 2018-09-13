FROM kennethreitz/pipenv
COPY ./app /app
RUN apt-get install -y cron rsyslog logrotate
COPY ./app/ingest/logrotate.conf /etc/logrotate.d/ingest
RUN mkdir /app/logs /app/ingest/config /app/ingest/data /app/ingest/debug 
RUN touch /var/log/cron.log
RUN ln -s /var/log/cron.log /app/logs/cron.log
RUN chmod +x /app/ingest/run.sh
RUN echo $'#!/bin/bash\n/usr/bin/python3 /app/ingest/testdata.py s1' > /etc/cron.hourly/sensordata
RUN chmod +x /etc/cron.hourly/sensordata
