.PHONY: help install run stop restart logs build clean deploy update status shell test

help: ## Mostra esta mensagem de ajuda
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Comandos Docker
build: ## Constrói a imagem Docker
	docker compose build

up: ## Inicia o bot em background
	docker compose up -d

down: ## Para o bot
	docker compose down

restart: ## Reinicia o bot
	docker compose restart

logs: ## Mostra logs em tempo real
	docker compose logs -f

logs-tail: ## Mostra últimas 50 linhas de log
	docker compose logs --tail=50

status: ## Mostra status do container
	docker compose ps

shell: ## Acessa o shell do container
	docker compose exec discord-bot sh

# Comandos Python Local
install: ## Instala dependências Python
	pip install -r requirements.txt

run: ## Executa o bot localmente
	python discord_bot.py

# Comandos de Desenvolvimento
dev: ## Inicia em modo desenvolvimento (rebuild + logs)
	docker compose up --build

rebuild: ## Reconstrói e reinicia o container
	docker compose up -d --build

# Comandos de Deploy
deploy: ## Deploy em produção (pull + rebuild)
	git pull origin main
	docker compose up -d --build

update: ## Atualiza o bot (alias para deploy)
	@make deploy

# Comandos de Limpeza
clean: ## Remove containers, volumes e imagens
	docker compose down -v
	docker system prune -f

clean-all: ## Remove tudo incluindo imagens
	docker compose down -v --rmi all
	docker system prune -af

# Comandos de Configuração
setup-env: ## Cria arquivo .env a partir do exemplo
	cp env.example .env
	@echo "Arquivo .env criado! Edite com suas credenciais."

# Comandos de Monitoramento
watch: ## Monitora logs continuamente
	watch -n 2 docker compose logs --tail=20

stats: ## Mostra estatísticas de uso do container
	docker stats cargonauta-bot
