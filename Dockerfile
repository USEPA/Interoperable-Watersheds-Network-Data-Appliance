FROM kennethreitz/pipenv

COPY ./api /app
COPY ./input /app/ingest
