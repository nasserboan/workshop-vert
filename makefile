.PHONY: help train format fix lint quality

help:
	@echo "Comandos disponíveis:"
	@echo ""
	@echo "  train     - Treina o modelo de ML"
	@echo "  format    - Formata o código com black"
	@echo "  fix       - Corrige problemas de linting com ruff"
	@echo "  lint      - Verifica qualidade do código"
	@echo "  quality   - Executa format + fix + lint"
	@echo "  help      - Mostra esta mensagem de ajuda"
	@echo ""

train:
	uv run python -m src.core.ml_model.train.train_handler

format:
	uv run black src/

fix:
	uv run ruff check --fix src/

lint:
	uv run ruff check src/

run-api:
	uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

quality: format fix lint