REQUIREMENTS="requirements-dev.txt"
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"


########################################################

.PHONY: all
all: test


.PHONY: init
init: uninstall
	@echo $(TAG)Installing dev requirements$(END)
	pip install --upgrade -r $(REQUIREMENTS)

	@echo $(TAG)Installing Agecalc$(END)
	pip install --upgrade --editable .

	@echo


.PHONY: clean
clean:
	@echo $(TAG)Cleaning up$(END)
	rm -rf .tox *.egg dist build .coverage .cache .pytest_cache agecalc.egg-info
	find . -name '__pycache__' -not -path './venv/*' -delete -print -o \
		   -name '*.pyc' -not -path './venv/*' -delete -print
	
	@echo


.PHONY: uninstall
uninstall:
	@echo $(TAG)Uninstalling Agecalc$(END)
	pip uninstall --yes agecalc &2>/dev/null

	@echo


.PHONY: test
test: init
	@echo $(TAG)Running tests with coverage $(END)
	pytest --cov ./agecalc --cov ./tests --doctest-modules --verbose ./tests
	
	@echo


.PHONY: test-reports
test-reports: init
	@echo $(TAG)Running tests and generating reports $(END)
	pytest --junitxml=test-reports/pytest.xml --cov ./agecalc --cov ./tests --doctest-modules --verbose ./tests
	
	@echo	


.PHONY: test-behave
test-behave: init
	@echo $(TAG)Running behave tests $(END)
	behave
	
	@echo

.PHONY: test-behave-reports
test-behave-reports: init
	@echo $(TAG)Running behave tests and generating reports $(END)
	behave --junit --junit-directory test-reports

	@echo

.PHONY: lint
lint:
	@echo $(TAG)Running lint $(END)
	pylint ./agecalc || true

	@echo
