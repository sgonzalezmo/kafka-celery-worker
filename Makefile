project := kafka_celery_worker

.DEFAULT_GOAL : help

help:
	@echo "bootstrap - initialize local environement for development. Requires virtualenv."
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "pylint - check code with pylint"
	@echo "pip-audit - check dependencies with pip-audit"
	@echo "pip-compile - compile dependencies with pip-compile"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "run - run application on uvicorn server"

check-virtual-env:
	@echo virtual-env: $${VIRTUAL_ENV?"Please run in virtual-env"}

bootstrap: check-virtual-env
	pip install -r requirements/dev.txt

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -rf {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f coverage.xml
	rm -fr htmlcov/

pylint:
	PYTHONPATH=src pylint $(project)

pip-audit:
	pip-audit -r requirements/dev.txt -r requirements/common.txt

pip-compile:
	pip-compile requirements/common.in

test:
	pytest

coverage: clean-test
	coverage run --include=src/$(project)/* -m pytest -m "not integtest"
	coverage report -m
	coverage html
	open htmlcov/index.html
