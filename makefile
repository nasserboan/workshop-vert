train:
	uv run python -m src.core.ml_model.train.train_handler

format:
	uv run black src/
	uv run ruff check src/

fix:
	uv run ruff check --fix src/

lint:
	uv run ruff check src/

quality: format fix lint