# Codex-trial-python


##Deploy

1. To start project — run (from the root folder): `docker-compose up -d`
2. To restore DB (Linux, Mac): `./scripts/db_restore.sh`


##Usage

###Getting car list
Car list is available here [GET]: `/api/car_list/`
To change pages [GET]: `/api/car_list/?page=4`

###Adding cars
Adding entrypoint [POST]: `/api/car_list/`
Data structure: 
```json
{ 
    "make": "str/max_128_char/required",
    "model": "str/max_128_char/required",
    "year": "str/max_4_char/required"
 }
```


###Running tests
To start tests — run (from the root folder): 
`docker exec -it <api container id> bash`
and then
`./manage.py test`