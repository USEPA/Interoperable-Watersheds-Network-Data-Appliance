FROM postgres
COPY ./scripts/apt.postgresql.org.sh /usr/bin/apt.postgresql.org.sh
RUN /usr/bin/apt.postgresql.org.sh
RUN apt-get install -y postgresql-10-cron
