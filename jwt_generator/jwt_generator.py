#!/usr/bin/env python
import os
import re
import json
import time
import click
import getpass
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa, rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from jwt import PyJWT


class JWTGenerator(object):

    def __init__(self):
        self.now = int(time.mktime(datetime.now().timetuple()))
        self.issuer = getpass.getuser()
        self.key = None
        self.not_before = 60
        self.expires_after = 30 * 60
        self.jwt = PyJWT()

    def load_private_key(self, private_key_file):
        with open(private_key_file, 'rb') as fh:
            pem_data = fh.read()
            self.set_private_key(pem_data)

    def set_private_key(self, pem_data):
        self.key = load_pem_private_key(
            pem_data, password=None, backend=default_backend())

    def has_expired(self, margin_in_seconds=30):
        now = int(time.mktime(datetime.now().timetuple()))
        return (self.now + self.expires_after - margin_in_seconds) < now

    def refresh_token(self):
        self.now = int(time.mktime(datetime.now().timetuple()))
        self.generate()

    def generate(self):
        message = {
            'iss': self.issuer,
            'nbf': self.now - self.not_before,
            'exp': self.now + self.expires_after
        }
        self.token = self.jwt.encode(message, self.key, 'RS256')

    @property
    def header(self):
        return 'Authorization: Bearer %s' % self.token


@click.command()
@click.option('--issuer',
              default=getpass.getuser(),
              help='of the token')
@click.option('--not-before',
              type=click.INT,
              default=60,
              help='number of seconds before now the token is no longer valid')
@click.option('--expires-after', type=click.INT, default=1800,
              help='number of seconds after which the token is no longer valid')
@click.option('--private-key-file',
              type=click.Path(exists=True, file_okay=True),
              default=os.path.expanduser('~/.ssh/id_rsa'),
              help='the private key file to sign the token with')
@click.option('--authorization-header', '-A',
              is_flag=True, default=False,
              help='print authorization header bearer token')
def main(
        issuer, not_before, expires_after, private_key_file,
        authorization_header):
    generator = JWTGenerator()
    generator.issuer = issuer
    generator.not_before = not_before
    generator.load_private_key(private_key_file)
    generator.generate()
    print(generator.header) if authorization_header else generator.token
