
# CodeLeap Backend Test

This project is a code test case made with Django Rest Framework, designed for managing careers posts (with CRUD operations).


## Setup

This project was made using Python3.11 and can be run using Docker (or Podman).

#### Step 1
Edit your secrets in .env (like database url, secret_key of Django) and configs (timezone, debug state)

Or, you can use the default config (that is made for the docker-compose.yaml). 
```
cp .env.example .env
```
#### Step 2

Once you've done the configuration of the project, if you need to run this project as bare-metal, run these commands

```
$ make bare-install
$ make bare-migrate
$ make bare-test
$ make bare-run
```

If you prefer to run using Docker, just run
```
$ make build 
$ make migrate
$ make test
$ make run
```

Once done, you can check the API reference documentation at `localhost:8000/api/schema/swagger-ui/`
