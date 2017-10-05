include Makefile.mk
USERNAME=mvanholsteijn
NAME=jwt-generator

do-build:
	python setup.py check
	python setup.py build
	
deploy:
	python setup.py sdist upload

clean:
	python setup.py clean

install:
	python setup.py install
