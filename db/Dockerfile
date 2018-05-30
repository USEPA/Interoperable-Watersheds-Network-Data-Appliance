FROM postgres
ENV POSTGRES_USER sos
ENV POSTGRES_PASSWORD sensors
ENV POSTGRES_DB ingest
RUN rm -fr /var/lib/apt/lists/* && apt-get clean && apt-get update && apt-get install -y postgis
