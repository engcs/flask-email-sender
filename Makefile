# -*- encoding: utf-8 -*-
# Copyright (c) 2022 - present

.PHONY: style, lint, isort, formatter
style:
	pycodestyle run.py
	pycodestyle ./apps
	pycodestyle ./scripts

lint: style
	pylint run.py
	pylint ./apps
	pylint ./scripts

isort:
	isort run.py
	isort ./apps
	isort ./scripts

formatter: isort
	blue run.py
	blue ./apps
	blue ./scripts