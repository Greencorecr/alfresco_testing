'''
Basic Tests for Alfresco, such as share availability, login tests, etc.
'''

import unittest
import requests

class BasicTest(unittest.TestCase):
    '''
    Class for Basic tests for Alfresco.
    '''

    def test_share_avl(self):
        '''
        Checking if the /share/ URL is available.
        Should return code 200.
        '''
        test_request = requests.get('https://localhost/share/', verify=False)
        self.assertEqual(test_request.status_code, 200)

    def test_alf_avl(self):
        '''
        Checking if the /alfresco/ URL is available.
        Should return code 200.
        '''
        test_request = requests.get('https://localhost/alfresco/', verify=False)
        self.assertEqual(test_request.status_code, 200)

    def test_share_redir_avl(self):
        '''
        Checking apropriate response for a non existent URL, from the proxy.
        Should return code 404.
        '''
        test_request = requests.get('https://localhost/nonexistent', verify=False)
        self.assertEqual(test_request.status_code, 404)

    def test_fail_avl(self):
        '''
        Checking apropriate response for a non existent URL, from tomcat.
        Should return code 404.
        '''
        test_request = requests.get('https://localhost/share/nonexistent', verify=False)
        self.assertEqual(test_request.status_code, 404)

    def test_alfresco_login(self):
        '''
        Testing logging into alfresco with a correct password.
        Should return code 200.
        '''
        url = 'https://localhost/alfresco/service/index'
        test_request = requests.get(url, auth=('admin', 'admin'), verify=False)
        self.assertEqual(test_request.status_code, 200)

    def test_alfresco_login_fail(self):
        '''
        Testing logging into alfresco with a wrong password.
        Should return code 401.
        '''
        url = 'https://localhost/alfresco/service/index'
        test_request = requests.get(url, auth=('admin', 'notadmin'), verify=False)
        self.assertEqual(test_request.status_code, 401)

    def test_share_login(self):
        '''
        Testing logging into share with a correct passowrd.
        Should return code 200.
        '''
        url = 'https://localhost/share'
        test_request = requests.get(url, auth=('admin', 'admin'), verify=False)
        self.assertEqual(test_request.status_code, 200)

#    def test_share_login_fail(self):
#        r = requests.get('https://localhost/share', auth=('admin', 'notadmin'), verify=False)
#        r.status_code
#        self.assertEqual(r.status_code, 401)

if __name__ == '__main__':
    unittest.main()
