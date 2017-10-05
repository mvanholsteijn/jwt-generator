include Makefile.mk
USERNAME=mvanholsteijn
NAME=jwt-generator

do-build:
	python setup.py check
	python setup.py build

push:
	python setup.py sdist
	twine upload dist/*

clean:
	rm -rf build/* 
	python setup.py clean

clobber: clean
	rm -rf dist/* 

install:
	python setup.py install
