# -*- encoding: utf-8 -*-
# Copyright (c) 2022 - present

.PHONY: style, lint, isort, formatter
style:
	pycodestyle run.py
	pycodestyle ./apps

lint: style
	pylint run.py
	pylint ./apps

isort:
	isort run.py
	isort ./apps

formatter: isort
	blue run.py
	blue ./apps