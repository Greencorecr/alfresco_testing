import unittest
import requests

class LdapTest(unittest.TestCase):

    def test_ldap(self):
        r = requests.get('https://localhost/alfresco/service/index', auth=('ldapuser', 'dogood'), verify=False)
        r.status_code
        self.assertEqual(r.status_code, 200)

    def test_ldap_login_fail(self):
        r = requests.get('https://localhost/alfresco/service/index', auth=('nouser', 'wrongpass'), verify=False)
        r.status_code
        self.assertEqual(r.status_code, 401)

if __name__ == '__main__':
    unittest.main()
