.PHONY: install test

defaul: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=./src pytest