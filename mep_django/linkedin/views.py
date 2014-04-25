from django.conf import settings
from django.template import RequestContext
from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse

from social.backends.linkedin import LinkedinOAuth

from social.apps.django_app.default.models import UserSocialAuth

# logs the user out, then redirects to the home page
def logout(request):
    auth_logout(request)
    return redirect('home')

# displays the home page
def home(request):
    print "displaying home"
    return render(request, 'home.html', {})

# displays the about page
def about(request):
    return render(request, 'about.html', {})

# displays the contact page
def contact(request):
    return render(request, 'contact.html', {})

