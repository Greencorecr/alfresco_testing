'''
Test for Alfresco, related to LDAP Authentication.
'''
import unittest
import requests

class LdapTest(unittest.TestCase):
    '''
    Class for testing Ldap auth in Alfresco
    '''
    def test_ldap(self):
        '''
        Tests a valid user created in the directory.
        Should return code 200.
        '''
        url = 'https://localhost/alfresco/service/index'
        test_request = requests.get(url, auth=('ldapuser@greencore.priv', 'dogood'), verify=False)
        self.assertEqual(test_request.status_code, 200)

    def test_ldap_login_fail(self):
        '''
        Tests an incorrect user, that does not exist in ldap.
        Should return code 401.
        '''
        url = 'https://localhost/alfresco/service/index'
        test_request = requests.get(url, auth=('nouser', 'wrongpass'), verify=False)
        self.assertEqual(test_request.status_code, 401)

if __name__ == '__main__':
    unittest.main()
