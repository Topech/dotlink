TOP_MODULE = dotlink

run:
	python3 -m $(TOP_MODULE)

init:
	pip install -r requirements.txt

test:
	python3 -m unittest tests/test_dotfile.py
	python3 -m unittest tests/test_linkmap.py
