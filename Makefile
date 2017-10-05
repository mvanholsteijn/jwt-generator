include Makefile.mk
USERNAME=mvanholsteijn
NAME=jwt-generator

do-build:
	python setup.py check
	python setup.py build
	
clean:
	python setup.py clean

install:
	python setup.py install

pre-tag:
	sed -e "s/^version=.*/version='$(VERSION)'/" -i "" setup.py
	git add setup.py
