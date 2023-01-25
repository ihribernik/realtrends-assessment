.PHONY: clean-pyc

help:
	@echo "clean - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "format - format with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "run - runserver with settings in .env file"
	@echo "run-dev - run in development mode [local]"
	@echo "run-dev - run in development mode [test]"
	@echo "run-dev - run in development mode [prod]"
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

testall:
	tox

run:
	 python manage.py runserver --settings=realTrendsAssessment.settings.development

run-dev:
	 python manage.py runserver --settings=realTrendsAssessment.settings.development

run-test:
	 python manage.py runserver --settings=realTrendsAssessment.settings.development

run-prod:
	 python manage.py runserver --settings=realTrendsAssessment.settings.development

run-docker:
	docker-compose up -d
