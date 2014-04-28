from django.conf import settings
from django.template import RequestContext
from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse

from social.backends.linkedin import LinkedinOAuth

from social.apps.django_app.default.models import UserSocialAuth


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

def news(request):
	"""displays the news page"""
	return render(request, 'news.html', {})
