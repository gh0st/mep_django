from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from linkedin import linkedin
from django.core.exceptions import PermissionDenied

API_KEY = '75l485e9k29snc'
API_SECRET = 'iw7fONMpJZcY5HOb'

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

def get_app(user):
    """Given a valid user object, return a LinkedInApplication instance that can be used to make the Linkedin API calls"""
    # Query user database to retrieve OAuth1 access tokens for the currently logged-in user"""
    social_user = user.social_auth.get()
    OAUTH_USER_TOKEN = social_user.extra_data['access_token']['oauth_token']
    OAUTH_USER_TOKEN_SECRET = social_user.extra_data['access_token']['oauth_token_secret'] 
    auth = linkedin.LinkedInDeveloperAuthentication(API_KEY, API_SECRET, OAUTH_USER_TOKEN, OAUTH_USER_TOKEN_SECRET, '', linkedin.PERMISSIONS.enums.values())
    return linkedin.LinkedInApplication(auth)

def discussions(request):
    """Displays the LinkedIn group content"""
    # handle unauthorized access with a 403
    if not request.user.is_authenticated() or not request.user.is_active:
        raise PermissionDenied
    # this is the ID of the linkedin group
    GROUP_ID = 1627067
    POST_SELECTORS = ['title', 'summary',  'creation-timestamp', 'site-group-post-url', 'creator', 'id',]
    app = get_app(request.user)
    group_posts = app.get_posts(GROUP_ID, selectors=POST_SELECTORS)
    return render(request, 'discussions.html', {'post_list':group_posts['values'],})

def news(request):
    """Diplays the LinkedIn company content, this is the critical view of the app"""
    # handle unauthorized access with a 403
    if not request.user.is_authenticated() or not request.user.is_active:
        raise PermissionDenied
    COMPANY_ID = 1035
    COMPANY_SELECTORS = ['name', 'id'] 
    app = get_app(request.user)    
    company = app.get_companies(company_ids=[COMPANY_ID], selectors=COMPANY_SELECTORS, params={'is-company-admin': 'true'})
    count = 10
    updates = app.get_company_updates(COMPANY_ID, params={'count': count, 'event-type': 'status-update',})
    
    update_list = []
    for update in updates['values']:
        my_dict = {'comment': update['updateContent']['companyStatusUpdate']['share']['comment']}
        if update['updateContent']['companyStatusUpdate']['share'].get('content'):
            my_dict['description'] = update['updateContent']['companyStatusUpdate']['share']['content'].get('description')
            my_dict['submittedImageUrl'] = update['updateContent']['companyStatusUpdate']['share']['content'].get('submittedImageUrl')
            my_dict['title'] = update['updateContent']['companyStatusUpdate']['share']['content'].get('title')
            my_dict['shortenedUrl'] = update['updateContent']['companyStatusUpdate']['share']['content'].get('shortenedUrl')
        update_list.append(my_dict)
    
    return render(request, 'news.html', {'update_list': update_list,})

