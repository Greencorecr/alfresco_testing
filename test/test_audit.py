import unittest
import requests

class AuditTest(unittest.TestCase):

    def test_audit(self):
        r = requests.get('https://localhost/alfresco/service/api/audit/control/', auth=('admin', 'admin'), verify=False)
        r.status_code
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
