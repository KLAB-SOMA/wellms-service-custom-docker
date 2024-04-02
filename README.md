# Wellms API + Klab

## Installation

### Postgres (default)

bash
```
cp docker/envs/.env.postgres.prod .env
```

_you can change the .env for one of the others provided for each type of necessity_


sh
```
make init
```

Great ! Now the API is served at api.localhost:1001 by this default config
For more information please access api.localhost:1001/api/documentation

## API Documentation

https://klab-soma.github.io/wellms-service-custom-docker/

## Demo & Credentials

| Role    | Email ID              | Password |
| ------- | --------------------- | -------- |
| Admin   | admin@escolalms.com   | secret   |
| Tutor   | tutor@escolalms.com   | secret   |
| Student | student@escolalms.com | secret   |
