.PHONY: reproduce notebook test check

reproduce:
	python analysis/python/reproduce_all.py

notebook:
	python analysis/python/check_notebook.py

test:
	python -m unittest discover -s tests -v

check: reproduce notebook test
