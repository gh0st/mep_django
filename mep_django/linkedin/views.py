from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from social.apps.django_app.default.models import UserSocialAuth
from linkedin import linkedin
#from django.http import HttpResponse


def logout(request):
    """logs the user out, then redirects to the home page"""
    auth_logout(request)
    return redirect('home')

def home(request):
    """displays the home page"""
    return render(request, 'home.html', {})


def about(request):
    """displays the about page"""
    return render(request, 'about.html', {})

def contact(request):
    """displays the contact page"""
    return render(request, 'contact.html', {})
    

def temp(request):
    """this is used for the popup window which houses the linkedin login page"""
    return render(request, 'temp.html', {})


def profile(request):
    """displays the user's profile page"""
    if request.user.is_authenticated():
        # since we're only using linked-in, this call returns a single instance
        social_user = request.user.social_auth.get()
        # retrieve data to pass to template
        name = social_user.extra_data['first_name'] + ' ' + social_user.extra_data['last_name']
        pic_url = social_user.extra_data['pic']
        headline = social_user.extra_data['headline']
        industry = social_user.extra_data['industry']
        
        ctx = {'name':name,
               'pic_url':pic_url,
               'headline':headline,
               'industry':industry,}
        return render(request, 'profile.html', ctx)
    else:
        return redirect('home')


def get_access_tokens(user):
    """Query user database to retrieve OAuth1 access tokens for the currently logged-in user"""
    social_user = user.social_auth.get()
    OAUTH_USER_TOKEN = social_user.extra_data['access_token']['oauth_token']
    OAUTH_USER_TOKEN_SECRET = social_user.extra_data['access_token']['oauth_token_secret']
    return (OAUTH_USER_TOKEN, OAUTH_USER_TOKEN_SECRET)

def news(request):
    if not request.user.is_authenticated():
        return redirect('home')
    
    API_KEY = '75l485e9k29snc'
    API_SECRET = 'iw7fONMpJZcY5HOb'
    USER_KEY, USER_SECRET = get_access_tokens(request.user)

    auth = linkedin.LinkedInDeveloperAuthentication(API_KEY, API_SECRET, USER_KEY, USER_SECRET, '', linkedin.PERMISSIONS.enums.values())
    
    app = linkedin.LinkedInApplication(auth)
    post_selectors = ['title', 'summary',  'creation-timestamp', 'site-group-post-url', 'creator', 'id',]
    
    posts = app.get_posts(1627067, selectors=post_selectors)
    '''
    for post in posts['values']:
        for k, v in post.iteritems():
            if k == 'creator':
                print 'Creator{'
                for k2, v2 in post['creator'].iteritems():
                    print '\t' + str(k2) + ': '
                    print '\t' + str(v2) + '\n'
                print '}'
            else:
                print str(k) + ': '
                print str(v) + '\n'
            #raw_input()
    '''
    return render(request, 'news.html', {'post_list':posts['values']})
    
