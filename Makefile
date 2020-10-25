TOP_MODULE = dotlink
PYTHON = python

run:
	python -m $(TOP_MODULE)

init:
	pip install -r requirements.txt

test:
	python -m unittest tests/test_dotfile.py
	python -m unittest tests/test_target.py
	python -m unittest tests/test_integration_dotfile_target.py
	#python -m unittest tests/test_linkmap.py
