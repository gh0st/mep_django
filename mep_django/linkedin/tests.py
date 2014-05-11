from django.test import TestCase
#from django.test import Client

class TestHomeView(TestCase):
    '''Unit test for the home view'''
    def setUp(self):
        pass

    def test_status_200(self):
        '''Return status 200 upon GET request'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class TestNewsView(TestCase):
    '''Unit test for the news view'''
    
    fixtures = ['fix1.json']

    def setUp(self):
        self.MY_URL = '/news/'

    def test_status_403(self):
        '''Return status 403 upon GET request when user is not logged in'''
        response = self.client.get(self.MY_URL)
        self.assertEqual(response.status_code, 403)

    def test_status_200(self):
        '''Return status 200 upon GET request when user IS logged in'''
        self.client.login(username='test', password='pass')
        response = self.client.get(self.MY_URL)
        self.assertEqual(response.status_code, 200)

