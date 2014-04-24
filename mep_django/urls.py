from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mep_django.linkedin.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'mep_django.linkedin.views.home'),
    url(r'^logout/$', 'mep_django.linkedin.views.logout'),
    url(r'^done/$', 'mep_django.linkedin.views.done', name='done'),
    url('', include('social.apps.django_app.urls', namespace='social')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
