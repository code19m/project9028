prod_run:
	docker compose -f docker-compose.prod.yml up -d --build

prod_down:
	docker compose -f docker-compose.prod.yml down

prod_logs:
	docker compose -f docker-compose.prod.yml logs -f $(name)

prod_exec:
	docker compose -f docker-compose.prod.yml -it exec $(name)

.PHONY: 'prod_run prod_down prod_logs prod_exec'
