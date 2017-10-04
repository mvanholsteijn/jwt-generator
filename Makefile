include Makefile.mk
USERNAME=mvanholsteijn
NAME=jwt-generator

on-tag:
	sed -e "s/^version=.*/version='$(VERSION)',/" -i "" setup.py
