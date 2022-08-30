SHELL := $(shell which bash)
MICROMAMBA := $(CURDIR)/.micromamba
MAMBA := $(MICROMAMBA)/micromamba
VENV := $(PWD)/.venv
DEPS := $(VENV)/.deps
PYTHON := $(VENV)/bin/python
PYTHON_CMD := PYTHONPATH=$(CURDIR) $(PYTHON)

.PHONY: test help

ifndef VERBOSE
.SILENT:
endif

help:
	grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

FORCE:

$(MAMBA):
	$(SHELL) ./install-micromamba.sh "$(MICROMAMBA)"

$(PYTHON): | $(MAMBA)
	$(MAMBA) create --quiet --yes -p $(VENV)

$(DEPS): environment.yml $(PYTHON)
	$(MAMBA) update --prune --quiet --yes -p $(VENV) -f environment.yml
	cp environment.yml $(DEPS)

.PHONY: deps
deps: $(DEPS)

clean:
	rm -rf $(VENV)
	rm -rf $(MICROMAMBA)
	find . -name __pycache__ | xargs rm -rf

test: $(DEPS)  ## Run tests
	$(PYTHON_CMD) -m pytest

repl: ## Run an iPython REPL
	$(VENV)/bin/ipython

run: $(DEPS) ## Run the program on the provided dataset
	cat data/chicago_beach_weather.csv | ./main

jupyter: $(DEPS) ## Run a jupyter notebook
	$(VENV)/bin/jupyter notebook

patch: ## Generate a patch file to submit for your solution
	git add .
	git diff --binary origin/master > aquatic_interview_solution.patch
