docker_start_postgres:
	docker-compose -f docker-compose.yaml up -d db

docker_stop_postgres:
	docker-compose -f docker-compose.yaml stop db

init_db_poetry:
	poetry run python init_db.py

run_poetry: docker_start_postgres init_db_poetry
	poetry run python -m app

init_db:
	python init_db.py

run: docker_start_postgres init_db
	python -m app

.PHONY: docker_start_postgres docker_stop_postgres init_db run