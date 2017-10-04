FROM python:2.7-alpine

COPY . /marathon-release
RUN  adduser -u 1000 -D user  && \
     cd /marathon-release && \
     python setup.py install

USER user
WORKDIR /home/user

ENTRYPOINT [ "/usr/local/bin/jwt-generator" ]
