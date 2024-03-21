# Wellms API + Klab

Laravel Headless LMS REST API customized by Klab

[![swagger](https://img.shields.io/badge/documentation-swagger-green)](https://escola-lms-api.stage.etd24.pl/api/documentation)
[![phpunit](https://github.com/EscolaLMS/API/actions/workflows/phpunit-tests.yml/badge.svg)](https://github.com/EscolaLMS/API/actions/workflows/phpunit-tests.yml)
[![downloads](https://img.shields.io/packagist/dt/escolalms/api)](https://packagist.org/packages/escolalms/api)
[![downloads](https://img.shields.io/packagist/v/escolalms/api)](https://packagist.org/packages/escolalms/api)
[![downloads](https://img.shields.io/packagist/l/escolalms/api)](https://packagist.org/packages/escolalms/api)
[![Maintainability](https://api.codeclimate.com/v1/badges/68b4fbde49bcd465e482/maintainability)](https://codeclimate.com/github/EscolaLMS/API/maintainability)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FEscolaLMS%2FAPI.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FEscolaLMS%2FAPI?ref=badge_shield)

## Packages

List of all packages is available at [packagist.org/?query=escolalms](https://packagist.org/?query=escolalms).

![Packages](https://github.com/EscolaLMS/.github/raw/main/deptrac-modules.png "Wellms Packages")

## Installation

### Postgres (default)

```bash
cp docker/envs/.env.postgres.prod .env
```

_you can change the .env for one of the others provided for each type of necessity_


```sh
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

## Test

Just run `phpunit` to test all the packages.

There are hundreds of tests in the packages and they are divided into:

### Integration packages test

Each packge contains their own php integration test this repo runs all of the

To run use `./vendor/bin/phpunit`

### End-to-end tests

[Cypress.io](https://docs.cypress.io/) is running end-to-end tests

To launch those use `yarn && yarn run cypress open`

You can see the results in the [cypress dashboard](https://dashboard.cypress.io/projects/kmx5cw/runs) including video artifacts

## Tasks

See [makefile](makefile) for all available devops tasks

- `make test-phpunit`
- `make bash`
- `make composer-update`
- `make swagger-generate`
- `make migrate-fresh`
- `make switch-to-postgres`
- `make switch-to-mysql`
- `make migrate-mysql`
- `make migrate-postgres`
- `make test-phpunit-postgres`
- `make test-phpunit-mysql`
- `make init`
- `make init-mysql`
- `make init-postgres`

## License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FEscolaLMS%2FAPI.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FEscolaLMS%2FAPI?ref=badge_large)
