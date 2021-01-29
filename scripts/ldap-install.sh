#/usr/bin/env bash

apt install -qy npm ldap-utils

npm install ldap-server-mock

cat << EOF | tee ldap-server-mock-conf.json
{
  "port": 3004,
  "userLoginAttribute": "cn",
  "searchBase": "dc=test",
  "searchFilter": "(&(objectclass=person)(cn={{username}}))"
}
EOF

cat << EOF | tee users.json
[
  {
    "dn": "cn=user,dc=test",
    "cn": "user-login",
    "attribute1": "value1",
    "attribute2": "value2"
  }
]
EOF

node node_modules/ldap-server-mock/server.js --conf=./ldap-server-mock-conf.json --database=./users.json &

