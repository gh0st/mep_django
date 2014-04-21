from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mep_django.linkedin.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup-email/', 'mep_django.linkedin.views.signup_email'),
    url(r'^email-sent/', 'mep_django.linkedin.views.validation_sent'),
    url(r'^login/$', 'mep_django.linkedin.views.home'),
    url(r'^logout/$', 'mep_django.linkedin.views.logout'),
    url(r'^done/$', 'mep_django.linkedin.views.done', name='done'),
    url(r'^email/$', 'mep_django.linkedin.views.require_email', name='require_email'),
    url(r'^myindex/', 'mep_django.linkedin.views.myindex', name='myindex'),
    url('', include('social.apps.django_app.urls', namespace='social')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)