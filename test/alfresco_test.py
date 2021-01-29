import unittest
import requests

class ShareTest(unittest.TestCase):

    def test_share_avl(self):
        r = requests.get('http://localhost/share/')
        r.status_code
        self.assertEqual(r.status_code, 200)

    def test_alf_avl(self):
        r = requests.get('http://localhost/alfresco/')
        r.status_code
        self.assertEqual(r.status_code, 200)

    def test_share_redir_avl(self):
        r = requests.get('http://localhost/nonexistent')
        r.status_code
        self.assertEqual(r.status_code, 200)

    def test_fail_avl(self):
        r = requests.get('http://localhost/share/nonexistent')
        r.status_code
        self.assertEqual(r.status_code, 404)

    def test_share_login(self):
        r = requests.get('http://localhost/alfresco/service/index', auth=('admin', 'admin'))
        r.status_code
        self.assertEqual(r.status_code, 200)

    def test_share_login_fail(self):
        r = requests.get('http://localhost/alfresco/service/index', auth=('admin', 'notadmin'))
        r.status_code
        self.assertEqual(r.status_code, 401)

if __name__ == '__main__':
    unittest.main()


