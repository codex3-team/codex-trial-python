#!/bin/bash
docker_postgres_container=$(docker ps -aqf "name=codex-trial-db")
docker exec -i $docker_postgres_container pg_restore -c -h localhost -U test -F c -d test ./backup/cars.tar.gz




