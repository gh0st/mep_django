from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social import exceptions as social_exceptions
from django.shortcuts import render

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if hasattr(social_exceptions, 'AuthCanceled'):
            return render(request, 'home.html', {'login':False,})
        else:
            raise exception

