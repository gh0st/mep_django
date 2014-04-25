from django.conf import settings
from django.template import RequestContext
from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse

from social.backends.linkedin import LinkedinOAuth

from social.apps.django_app.default.models import UserSocialAuth

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('home.html', {
        'login' : False,
    }, RequestContext(request))

def home(request):
    print "displaying home"
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

