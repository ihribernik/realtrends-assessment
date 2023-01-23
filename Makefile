.PHONY: clean-pyc

help:
	@echo "clean - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "format - format with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "run-dev - run in development mode [local]"
	@echo "run-docker - run in development mode [docker instance]"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	rm -rf .tox +
	rm -rf .pytest_cache

lint:
	flake8 products realTrendsAssessment tests

format:
	black products realTrendsAssessment tests

test:
	tox

#coverage:
#	...

run-dev:
	 python manage.py runserver --settings=realTrendsAssessment.settings.development

run-docker:
	docker-compose up -d
