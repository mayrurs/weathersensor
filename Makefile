# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

all: down build up 

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

unit-test:
	docker-compose run --rm --no-deps --entrypoint=pytest sensor /tests/unit

logs:
	docker-compose logs sensor
