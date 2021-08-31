SHELL := $(shell which bash)
MINICONDA := $(CURDIR)/.miniconda3
CONDA := $(MINICONDA)/bin/conda
CONDA_VERSION := 4.7.10
VENV := $(PWD)/.venv
DEPS := $(VENV)/.deps
PYTHON := $(VENV)/bin/python
PYTHON_CMD := PYTHONPATH=$(CURDIR) $(PYTHON)

.PHONY: test help

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
	MINICONDA_URL := https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
endif
ifeq ($(UNAME_S),Darwin)
	MINICONDA_URL := https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
endif

ifndef VERBOSE
.SILENT:
endif

help:
	grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

FORCE:

$(CONDA):
	echo "Installing Miniconda3 to $(MINICONDA)"
	curl ${MINICONDA_URL} > $(CURDIR)/miniconda.sh
	bash $(CURDIR)/miniconda.sh -u -b -p "$(CURDIR)/.miniconda3"
	rm $(CURDIR)/miniconda.sh

$(PYTHON): | $(CONDA)
	$(CONDA) env create -p $(VENV)

$(DEPS): environment.yml $(PYTHON)
	$(CONDA) env update --prune --quiet -p $(VENV) -f environment.yml
	cp environment.yml $(DEPS)

clean:
	rm -rf $(VENV)
	rm -rf $(MINICONDA)
	find . -name __pycache__ | xargs rm -rf

test: $(DEPS)  ## Run tests
	$(PYTHON_CMD) -m pytest

watch: $(DEPS) ## Run unit tests continuously
	$(PYTHON_CMD) -mpytest_watch

repl: ## Run an iPython REPL
	$(VENV)/bin/ipython

run: $(DEPS) ## Run the program on the provided dataset
	cat data/chicago_beach_weather.csv | ./main

jupyter: $(DEPS) ## Run a jupyter notebook
	$(VENV)/bin/jupyter notebook

patch: ## Generate a patch file to submit for your solution
	git add .
	git diff --binary origin/master > aquatic_interview_solution.patch
