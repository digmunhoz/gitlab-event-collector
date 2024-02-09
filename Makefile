
start:
	@docker-compose up -d elasticsearch kibana grafana

build:
	@docker-compose build

run:
	@docker-compose run collector

stop:
	@docker-compose down -v

logs:
	@docker-compose logs -f

status:
	@docker-compose ps