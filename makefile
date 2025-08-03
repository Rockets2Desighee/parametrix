# === Makefile for Parametrix ===

# Python virtual environment name (optional override via env)
VENV ?= venv_parametrix
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# --- Setup and Environment ---
.PHONY: setup install freeze clean clean-pyc

setup:
	python3.11 -m venv $(VENV)
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r requirements.txt

install:
	$(PIP) install -r requirements.txt

freeze:
	$(PIP) freeze > env/pinned_requirements.txt

clean:
	rm -rf $(VENV) __pycache__ .pytest_cache .mypy_cache *.egg-info .coverage htmlcov

clean-pyc:
	find . -name '*.pyc' -o -name '*.pyo' -o -name '__pycache__' | xargs rm -rf

# --- Linting, Formatting, Type Checking ---
.PHONY: lint format typecheck lint-full

format:
	black src/ tests/
	isort src/ tests/

lint:
	flake8 src/ tests/

lint-full:
	pylint src/parametrix/ tests/

typecheck:
	mypy src/parametrix/

# --- Testing ---
.PHONY: test coverage

test:
	pytest tests/

coverage:
	pytest --cov=src/parametrix --cov-report=term --cov-report=html tests/

# --- Run Pipelines or Triggers ---
.PHONY: run run-triggers

run:
	$(PYTHON) scripts/run_pipeline.py

run-triggers:
	$(PYTHON) src/parametrix/core/trigger_runner.py

# --- Jupyter Kernel Registration ---
.PHONY: kernel

kernel:
	$(PYTHON) -m ipykernel install --user --name=$(VENV) --display-name "Python (Parametrix)"

# --- Git Hooks ---
.PHONY: hooks

hooks:
	pre-commit install

# --- Default Target ---
default: install
