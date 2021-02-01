import unittest
import requests

class ShareTest(unittest.TestCase):

    def test_share_avl(self):
        r = requests.get('http://localhost/share/', verify=False)
        r.status_code
        self.assertEqual(r.status_code, 200)

    def test_alf_avl(self):
        r = requests.get('http://localhost/alfresco/', verify=False)
        r.status_code
        self.assertEqual(r.status_code, 200)

    def test_share_redir_avl(self):
        r = requests.get('http://localhost/nonexistent', verify=False)
        r.status_code
        self.assertEqual(r.status_code, 200)

    def test_fail_avl(self):
        r = requests.get('http://localhost/share/nonexistent', verify=False)
        r.status_code
        self.assertEqual(r.status_code, 404)

    def test_share_login(self):
        r = requests.get('http://localhost/alfresco/service/index', auth=('admin', 'admin'), verify=False)
        r.status_code
        self.assertEqual(r.status_code, 200)

    def test_share_login_fail(self):
        r = requests.get('http://localhost/alfresco/service/index', auth=('admin', 'notadmin'), verify=False)
        r.status_code
        self.assertEqual(r.status_code, 401)

if __name__ == '__main__':
    unittest.main()


