#/bin/bash
docker-compose down
docker volume rm ingest_datavol
docker rmi 'ingest_database'
