'''
Tests for Alfresco, related to the Audit module.
'''

import unittest
import requests

class AuditTest(unittest.TestCase):
    '''
    Class for Testing the Audit module in Alfresco.
    '''

    def test_audit(self):
        '''
        Checking availability for an Audit URL. Needs auth.
        Should return code 200.
        '''
        url = 'https://localhost/alfresco/service/api/audit/control/'
        test_request = requests.get(url, auth=('admin', 'admin'), verify=False)
        self.assertEqual(test_request.status_code, 200)

if __name__ == '__main__':
    unittest.main()
