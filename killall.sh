#/bin/bash
docker-compose down
docker volume rm ingest_datavol
docker rmi 'ingest_database'
docker rmi 'ingest_sos'
docker rmi 'ingest_api'
