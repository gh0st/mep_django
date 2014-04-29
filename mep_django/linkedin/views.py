from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from social.apps.django_app.default.models import UserSocialAuth
from linkedin import linkedin
from django.http import HttpResponse

# logs the user out, then redirects to the home page
def logout(request):
    auth_logout(request)
    return redirect('home')

# displays the home page
def home(request):
    return render(request, 'home.html', {})

# displays the about page
def about(request):
    return render(request, 'about.html', {})

# displays the contact page
def contact(request):
    return render(request, 'contact.html', {})

# displays the user's profile page
def profile(request):
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

# Query user database to retrieve OAuth1 access tokens for the
# currently logged-in user
def get_access_tokens(user):
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
    #profile = app.get_profile()
    post_selectors = ['title', 'summary']
    posts = app.get_posts(1627067, selectors=post_selectors)
    return HttpResponse(str(posts))

