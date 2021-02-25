#!/bin/bash
docker exec -i $(docker ps -aqf "name=test-db") psql -h localhost -U postgres -d cdx -f ./cars.sql