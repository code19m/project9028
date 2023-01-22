run:
	docker compose up -d --build

down:
	docker compose down

restart:
	docker compose down
	docker compose up -d --build

logs:
	docker compose logs -f $(name)

exec:
	docker compose exec -it $(name) bash

prod_run:
	docker compose -f docker-compose.prod.yml up -d --build

prod_down:
	docker compose -f docker-compose.prod.yml down

prod_restart:
	docker compose -f docker-compose.prod.yml down
	docker compose -f docker-compose.prod.yml up -d --build

prod_logs:
	docker compose -f docker-compose.prod.yml logs -f $(name)

prod_exec:
	docker compose -f docker-compose.prod.yml exec -it $(name) bash

.PHONY: 'run down restart logs exec prod_run prod_down prod_logs prod_exec'
