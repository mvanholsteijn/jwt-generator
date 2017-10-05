A simple command line jwt token generator based on a rsa private key.

By default it will print a JWT token with iss, nbf and exp set which is signed 
by the private key in ~/.ssh/id_rsa.::

	iss - will be set to the current user name 
	nbf - will be set to 1 minute in the past
	exp - will be set to 30 minutes in the future.

You can override the default settings on the command line.

**Options**

--issuer TEXT               of the token
--not-before INTEGER        number of seconds before now the token is no longer valid
--expires-after INTEGER     number of seconds after which the token is no longer valid
--private-key-file PATH     the private key file to sign the token with
-A, --authorization-header  print authorization header bearer token
--help                      Show this message and exit.

**Example**

To send the the authorization bearer token with curl, type::

	curl -H "$(jwt-generator -A)" https://httpbin.org/headers

**Install on MacOS**

To install you MacOs you might run into trouble due to the dependency on cryptography. Type:::

	export LDFLAGS="-L/usr/local/opt/openssl/lib"
	export CPPFLAGS="-I/usr/local/opt/openssl/include"
	export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"

before you do the `pip install jwt-generator`. See https://github.com/pyca/cryptography/issues/2692 for details.
