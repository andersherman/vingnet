up:
	docker compose up

down:
	docker compose down

build:
	docker compose build

cleanup:
	docker-compose down --remove-orphans

rebuild-fastapi-example:
	docker-compose up -d --no-deps --build <service_name>
