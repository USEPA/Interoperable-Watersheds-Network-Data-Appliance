FROM mdillon/postgis
ENV POSTGRES_USER sos 
ENV POSTGRES_PASSWORD sensors
ENV POSTGRES_DB ingest
COPY ./scripts/apt.postgresql.org.sh /usr/bin/apt.postgresql.org.sh
RUN /usr/bin/apt.postgresql.org.sh
RUN apt-get install -y postgresql-10-cron
