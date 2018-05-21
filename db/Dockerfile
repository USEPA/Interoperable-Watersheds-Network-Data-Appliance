FROM postgres
ENV POSTGRES_USER sos 
ENV POSTGRES_PASSWORD sensors
ENV POSTGRES_DB ingest
COPY ./scripts/apt.postgresql.org.sh /usr/bin/apt.postgresql.org.sh
RUN /usr/bin/apt.postgresql.org.sh
RUN apt-get install -y postgis
RUN apt-get install -y postgresql-10-cron
RUN apt-get install -y postgresql-plpython-10
RUN apt-get install -y python3-pip
RUN pip3 install python-dateutil
