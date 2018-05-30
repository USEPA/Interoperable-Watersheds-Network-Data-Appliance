FROM mdillon/postgis
ENV POSTGRES_USER sos
ENV POSTGRES_PASSWORD sensors
ENV POSTGRES_DB ingest
COPY ./scripts /docker-entrypoint-initdb.d/
