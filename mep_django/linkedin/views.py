from django.conf import settings
from django.template import RequestContext
from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse

from social.apps.django_app.default.models import UserSocialAuth
from social.backends.linkedin import LinkedinOAuth

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('home.html', {
        'login' : False,
    }, RequestContext(request))

def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    #return render_to_response('home.html', {
    '''
    return render_to_response('<script type="text/javascript">window.close(); window.parent.location.href="home.html";</script>', 'home.html', {
        #'linkedin_id': getattr(settings, 'SOCIAL_AUTH_LINKEDIN_KEY', None),
        'login' : False,
    }, RequestContext(request))
    '''
    return HttpResponse('<script type="text/javascript">window.close(); window.parent.location.href="done";</script>')

@login_required
def done(request):
    """Login complete view, displays user data"""
    # scope = ' '.join(settings.SOCIAL_AUTH_LINKEDIN_SCOPE)
    # get UserSocialAuth object related to loggin-in auth.User object
    # social_user = UserSocialAuth.objects.get(user_id=request.user.id)
    return render_to_response('home.html', {
        'name' : request.user.first_name,
        'login' : True,
    }, RequestContext(request))
