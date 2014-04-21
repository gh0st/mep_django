from django.conf import settings
from django.template import RequestContext
from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse

from social.backends.linkedin import LinkedinOAuth

from social.apps.django_app.default.models import UserSocialAuth
import json

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('home.html', {}, RequestContext(request))

def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return render_to_response('home.html', {
        #'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None)
        'linkedin_id': getattr(settings, 'SOCIAL_AUTH_LINKEDIN_KEY', None)
    }, RequestContext(request))

@login_required
def done(request):
    """Login complete view, displays user data"""
    scope = ' '.join(settings.SOCIAL_AUTH_LINKEDIN_SCOPE)
    # get UserSocialAuth object related to loggin-in auth.User object
    social_user = UserSocialAuth.objects.get(user_id=request.user.id)
    print type(social_user.extra_data)
    print social_user.extra_data
    return render_to_response('done.html', {
        'user': request.user,
        'extra_data': social_user.extra_data,
        'linkedin_id': getattr(settings, 'SOCIAL_AUTH_LINKED_IN_KEY', None),
        'linkedin_scope': scope
    }, RequestContext(request))

def signup_email(request):
    return render_to_response('email_signup.html', {}, RequestContext(request))


def validation_sent(request):
    return render_to_response('validation_sent.html', {
        'email': request.session.get('email_validation_address')
    }, RequestContext(request))


def require_email(request):
    if request.method == 'POST':
        request.session['saved_email'] = request.POST.get('email')
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)
    return render_to_response('email.html', RequestContext(request))
