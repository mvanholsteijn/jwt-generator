A simple command line jwt token generator based on a rsa private key.

By default it will print a JWT token with iss, nbf and exp set which is signed 
by the private key in ~/.ssh/id_rsa.

::
    iss - will be set to the current user name 
    nbf - will be set to 1 minute in the past
    exp - will be set to 30 minutes in the future.

You can override the default settings on the command line.

::
    Usage: jwt-generator [OPTIONS]

    Options:
      --issuer TEXT               of the token
      --not-before INTEGER        number of seconds before now the token is no longer valid
      --expires-after INTEGER     number of seconds after which the token is no longer valid
      --private-key-file PATH     the private key file to sign the token with
      -A, --authorization-header  print authorization header bearer token
      --help                      Show this message and exit.

Example
-------
::
    curl -H "$(jwt-generator -A)" https://httpbin.org/headers