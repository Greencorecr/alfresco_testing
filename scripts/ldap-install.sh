#/usr/bin/env bash

apt install -qy ldap-utils

wget -O glauth https://github.com/glauth/glauth/releases/download/v1.1.2/glauth64
chmod +x glauth

(mkdir certs/ && cd certs && openssl req -x509 -nodes -days 365 -subj "/C=CA/ST=QC/O=Company, Inc./CN=newdomain.com" -addext "subjectAltName=DNS:newdomain.com" -newkey rsa:2048 -out server.crt -keyout server.key )

cat << EOF | tee glauth.cfg
[ldap]
  enabled = true
  listen = "0.0.0.0:389"
[ldaps]
  enabled = true
  listen = "0.0.0.0:636"
  cert = "certs/server.crt"
  key = "certs/server.key"
[backend]
  datastore = "config"
  baseDN = "dc=greencore,dc=priv"
[[users]]
  name = "ldapuser"
  unixid = 5001
  primarygroup = 5501
  passsha256 = "6478579e37aff45f013e14eeb30b3cc56c72ccdc310123bcdf53e0333e3f416a" # dogood
[[groups]]
  name = "ldapgroup"
  unixid = 5501
EOF

./glauth -c glauth.cfg  &
