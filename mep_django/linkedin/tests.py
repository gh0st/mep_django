from django.test import TestCase
import views
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest

class TestHomeView(TestCase):
    '''Unit test for the home view'''
    def setUp(self):
        self.MY_URL = '/'

    def test_found_right_view(self):
        '''Test that the URL maps to the right view function'''
        self.assertEqual(resolve(self.MY_URL).func, views.home)

    def test_status_200(self):
        '''Return status 200 upon GET request'''
        response = self.client.get(self.MY_URL)
        self.assertEqual(response.status_code, 200)

"""
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
"""

class TestDiscussionsView(TestCase):
    '''Unit test for the home view'''

    #fixtures = [ 'fix1.json' ]

    def setUp(self):
        self.MY_URL = '/discussions/'

    def test_found_right_view(self):
        '''Test that the URL maps to the right view function'''
        self.assertEqual(resolve(self.MY_URL).func, views.discussions)

    def test_status_403(self):
        '''Return status 403 upon GET request when user is not logged in'''
        response = self.client.get(self.MY_URL)
        self.assertEqual(response.status_code, 403)

class TestNewsView(TestCase):
    '''Unit test for the home view'''
    def setUp(self):
        self.MY_URL = '/news/'

    def test_found_right_view(self):
        '''Test that the URL maps to the right view function'''
        self.assertEqual(resolve(self.MY_URL).func, views.news)

    def test_status_403(self):
        '''Return status 403 upon GET request when user is not logged in'''
        response = self.client.get(self.MY_URL)
        self.assertEqual(response.status_code, 403)

class TestAboutView(TestCase):
    '''Unit test for the about view'''
    def setUp(self):
        self.MY_URL = '/about/'

    def test_found_right_view(self):
        '''Test that the URL maps to the right view function'''
        self.assertEqual(resolve(self.MY_URL).func, views.about)

    def test_status_200(self):
        '''Return status 200 upon GET request'''
        response = self.client.get(self.MY_URL)
        self.assertEqual(response.status_code, 200)

class TestContactView(TestCase):
    '''Unit test for the contact view'''
    def setUp(self):
        self.MY_URL = '/contact/'

    def test_found_right_view(self):
        '''Test that the URL maps to the right view function'''
        self.assertEqual(resolve(self.MY_URL).func, views.contact)

    def test_status_200(self):
        '''Return status 200 upon GET request'''
        response = self.client.get(self.MY_URL)
        self.assertEqual(response.status_code, 200)

