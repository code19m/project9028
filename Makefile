prod_run:
	docker compose -f docker-compose.prod.yml up -d --build

prod_logs:
	docker compose -f docker-compose.prod.yml logs -f $(name)

prod_down:
	docker compose -f docker-compose.prod.yml down

.PHONY: 'prod_run prod_logs prod_down'
